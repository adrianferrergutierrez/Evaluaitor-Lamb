# Agents All the Way Down — Metodología

> Resumen del paper de Marc Alier Forment et al. (2026) para uso como contexto de agente.

---

## Resumen ejecutivo

**Agents All the Way Down** es una metodología en cinco fases para construir agentes de IA personalizados desde cero, sin depender de frameworks. El argumento central: los frameworks enseñan su propia API, no los principios. Un agente construido con esta metodología es más simple, más barato de evolucionar y más seguro frente a ataques de cadena de suministro.

---

## Fase P1 — Substrate (Sustrato)

**Claim:** El ingeniero debe internalizar el LLM como componente de software, no solo "usar la API correctamente".

### La lente estructural
Cada llamada LLM compone tres secciones en orden estricto:

```
[ tools ]    ← declarados al init del agente; más estables; mayor cache
[ system ]   ← fijado al inicio de sesión; estable por sesión; cacheado
[ messages ] ← crecen por turno; solo los últimos son tokens frescos
```

### Implicaciones del KV-cache
1. La **volatilidad aumenta de arriba a abajo**. Los elementos estables deben estar arriba para aprovechar el cache.
2. Cualquier cambio en `tools` o `system` **invalida el cache** aguas abajo. Reordenar herramientas alfabéticamente puede destruir el cache de toda una sesión.
3. Los cache hits cuestan ~10× menos que tokens frescos (Anthropic: 0.1×, OpenAI: 0.1–0.5×, Gemini: 0.25×/0.1×, DeepSeek: 0.1×).

### Disciplina KV-cache
- `tools` se declaran **una vez en el init** e inmutables durante la sesión.
- `system` se fija una vez al inicio y contiene: ejemplos one-shot de uso de herramientas, conocimiento de dominio, persona, directivas, memorias.
- `messages` crece **solo en modo append** — nunca reescribir, nunca splice, nunca pop.
- **Cache poisons** (timestamps, estado runtime, pregunta actual del usuario) **fuera del system prompt**.

### Anti-mandatos P1
- No poner contexto dinámico (timestamps, estado runtime) en el system prompt.
- No "limpiar" tools o system entre sesiones si no hay cambio funcional.

---

## Fase P2 — Building Blocks (Bloques de construcción)

### Function calling
El ciclo fundamental del agente: `prompt → tool call → ejecución → resultado → siguiente prompt`.

Tres preocupaciones operativas:
- **Tool-count problem**: 5 herramientas está bien, 30 no — el modelo pierde foco y el catálogo consume tokens.
- **Schema design**: operaciones atómicas, descripciones de calidad de documentación, parámetros JSON-Schema limpios, modos de fallo elegantes.
- **Seguridad**: nunca en el schema, nunca en la descripción, nunca en el system prompt — **siempre en el dispatcher del scaffolding**.

### MCP vs CLI vs liteshell

**El LLM ya conoce bash.** Preentrenado en ejemplos de shell Linux, el modelo puede manejar un CLI nuevo ejecutando `--help`. MCP no tiene ese preentrenamiento gratuito.

Regla operativa: **si puedes hacerlo con un CLI, hazlo con el CLI** — es más rápido, más barato y reemplazable sin reentrenar al modelo.

**Liteshell**: cuando el agente corre dentro de una aplicación cloud (FastAPI, Django, etc.) sin acceso a shell, el liteshell es una pequeña clase Python que expone las operaciones de tu aplicación como una superficie tipo shell, presentada al modelo a través de una herramienta `call_cli` y un skill en markdown que describe la gramática de invocación.

### El agent loop (~30 líneas, sin framework)

```python
messages = []
while True:
    response = llm.chat(
        tools=tools,          # estático, declarado en init
        system=system_prompt, # estático, fijado al inicio de sesión
        messages=messages,    # crece solo en append
    )
    if not response.tool_calls:
        return response.content
    for tc in response.tool_calls:
        result = dispatch(tc)  # responsabilidad del scaffolding
    messages.append(assistant_turn(tc))
    messages.append(tool_result(result))
```

> **Frontera clave**: el LLM piensa y decide; el scaffolding hace todo lo demás.

### Skills, Characters, Instruction Sets
Viven en el system prompt:
- **Skills**: archivos markdown que describen cómo hacer algo específico. Editables sin tocar código.
- **Characters**: voz/registro/postura — el lever de precisión más barato disponible.
- **Instruction Sets**: reglas (must-dos y must-not-dos). **Nunca poner seguridad aquí** — las instrucciones moldean el comportamiento; el allow-list del scaffolding moldea los resultados.

### Anti-mandatos P2
- No usar un framework para aprender estos bloques. El framework los ejecutará correctamente; tus manos no aprenderán los principios.

---

## Fase P3 — Prototype with a General-Purpose Agent

**El movimiento**: usar un agente de propósito general (Claude Code, OpenCode, Cursor) como pair-programming partner y herramienta de reconocimiento, con el objetivo explícito de construir un agente personalizado para tu aplicación específica.

### El paso de reconocimiento
Antes de escribir código del agente personalizado, el agente de propósito general inspecciona la plataforma donde vas a construir. Esto expone qué falta antes de que empiece el diseño del agente personalizado.

### Architecture-discovered-by-building
El movimiento clásico de ingeniería es diseñar la arquitectura primero. **El movimiento de la metodología es construir primero** y dejar que la arquitectura emerja de lo que funciona y lo que no. Tres cosas que descubres así:
- Dónde viven realmente tus datos (a menudo no donde dice el diagrama de diseño).
- Qué superficie de herramientas puede manejar el LLM limpiamente (a menudo más gruesa que la API real de la plataforma).
- Dónde pertenece el límite de seguridad (casi siempre en el dispatch de herramientas del scaffolding, no en el prompt).

### Herramientas y seguridad en P3
- El dispatch de herramientas está en **tu código, no en el texto del modelo**.
- **Allow-list todo** — el modelo puede pedir `call_cli ls /tmp`; tu código decide si `ls /tmp` está permitido.
- Las credenciales nunca viajan como strings — keychain del SO, variables de entorno en el runtime, **nunca en el system prompt, nunca en argumentos de herramientas**.
- **Regla dura**: las API keys nunca deben viajar sobre HTTP.

### Entregables de P3
- Prototipo funcional contra la plataforma real.
- Lista de herramientas necesarias (CLIs existentes + entradas nuevas de liteshell).
- Primer borrador del system prompt con uno o dos skills cargados.
- Lista documentada de gaps (APIs faltantes, preguntas de límite de seguridad).

### Anti-mandatos P3
- No saltarse P3 porque "ya conoces la arquitectura". No la conoces. La arquitectura emerge del build.

---

## Fase P4 — Harvest, Fold, Ship as CLI (el Turtle Pattern)

P4 tiene tres movimientos: **harvest**, **fold** y **ship as CLI**.

### Harvest
Desde el prototipo de P3, recolectar deliberadamente:
- Herramientas (schemas + implementaciones → directorio `tools/` limpio).
- Scaffolding de seguridad (allow-list, setup de auth, política de autorización).
- Skills (promovidos de snippets sueltos a archivos markdown versionados).
- Characters (promovidos de frases experimentales a contenido de persona explícito).
- Instruction sets (reglas, la sección de directivas).

### Fold — el loop de ~30 líneas

```python
class Agent:
    def __init__(self, llm, tools, system_prompt, security):
        self.llm = llm
        self.tools = tools           # P2 building block
        self.system = system_prompt  # skills + character + directives
        self.security = security     # P3 allow-list, en scaffolding no en prompt
        self.session = SessionStore()

    def run(self, user_message, session_id=None):
        messages = self.session.load(session_id)
        messages.append({"role": "user", "content": user_message})
        while True:
            response = self.llm.chat(
                tools=self.tools.schemas,
                system=self.system,
                messages=messages,
            )
            messages.append(response.assistant_turn())
            if not response.tool_calls:
                self.session.save(session_id, messages)
                return response.content, session_id
            for tc in response.tool_calls:
                self.security.check(tc)  # lanza excepción si no está permitido
                result = self.tools.dispatch(tc)
                messages.append({"role": "tool", "content": result, ...})
```

### Ship as CLI — el Turtle Pattern

**El movimiento definitorio de P4**: tu agente es en sí mismo una herramienta CLI.

```bash
turtle "haz algo"
  → respuesta + nuevo-session-id

turtle <session-id> "haz lo siguiente"
  → continúa la sesión

turtle --list-sessions

turtle <session-id> --replay
  → re-ejecución determinista con el mismo LLM seed
```

El agente debe tener:
- **Invocación stateless** por llamada (el session store es la superficie de estado).
- **Continuación** con session-id para uso multi-turno.
- **Outputs estructurados** — la respuesta + session id + opcionalmente un JSON sidecar con trazas de herramientas.
- **`--help` que funciona** — tanto para lectores humanos como para el agente driver en P5.

> **Constraint de diseño**: el agente debe construirse para que sea friendly para que otro agente lo conduzca. Un despliegue en ventana de chat no es testeable por otro agente. Un CLI sí.

### Anti-mandatos P4
- **No poner seguridad en el prompt. Siempre.** (La lección más repetida del build AAC.)
- No hacer ship sin que `--help` funcione; estás quitando la superficie de onboarding del siguiente agente.

---

## Fase P5 — Agent-Tests-Agent

**El pilar nuevo**. El QA clásico (typing, unit tests, integration tests, e2e tests) fue desarrollado para software determinista. Los agentes son estocásticos; tienen una superficie de comportamiento que el QA clásico no puede testear limpiamente.

### El patrón
Un agente CLI de propósito general (Claude Code, OpenCode) recibe tres inputs:
1. Un **escenario** — descripción en lenguaje natural de una tarea que el agente personalizado debería poder manejar.
2. La **invocación CLI** del agente personalizado (la interfaz Turtle de P4).
3. Un **rubric de evaluación** describiendo qué cuenta como pass, qué como fail, qué casos edge probar.

El agente de propósito general conduce al agente personalizado a través del escenario, observa outputs y trazas de herramientas, prueba casos edge (inputs adversariales, peticiones ambiguas, drift multi-turno), y devuelve una evaluación estructurada: pass/fail por criterio, con evidencia del transcript.

### Qué da P5 que el QA clásico no puede dar
1. **Regression testing de comportamiento**: "¿Sigue el agente negándose a filtrar credenciales cuando se le pide de forma ingeniosa?" No es un unit test; es un test P5.
2. **LLM-comparison testing**: mismo escenario, diferente backbone — Claude Opus vs DeepSeek vs Qwen — produce comparación de comportamiento manzanas-con-manzanas.
3. **Generación de documentación como efecto secundario**: los transcripts del agente evaluador son ejemplos de interacciones; los buenos van a la documentación.
4. **El improvement loop**: los fallos revelan gaps; los gaps vuelven a P3 como prototipos de siguiente iteración.

### El stack QA completo

```
┌───────────────────────────┐
│       human review        │  ← gate final, lo mantiene el ingeniero
├───────────────────────────┤
│   agent-tests-agent (P5)  │  ← capa nueva
├───────────────────────────┤
│    integration tests      │
│       unit tests          │  ← SE clásico
│   typing / static checks  │
└───────────────────────────┘
            ↑
       el agente (el artifact)
```

Las capas clásicas testean que el plumbing es correcto (comportamiento determinista, sin excepciones, tipos coinciden). La capa P5 testea que **el comportamiento es correcto** (el agente hace lo que el usuario necesita, rechaza lo que debe rechazar, se recupera de lo que debe recuperarse). Ambas capas son obligatorias.

### Anti-mandatos P5
- No tratar P5 como algo puntual. P5 es continuo: cada cambio en tools, system prompt, skills o character re-ejecuta el suite de escenarios.
- No saltarse P5 porque "testeé las herramientas individualmente" — testear las herramientas es unit testing; agent-tests-agent es behavioral testing; no son sustitutos.

---

## La construcción circular (§4)

La metodología es circular por construcción:

```
P3 ── prototipo ──► P4 ── ship CLI ──► P5
                                        │
                                        │ gap list
                                        ▼
                         ┌── siguiente iteración ┘
                         │
                         ▼
                         P3 ──────────────►
```

P5 produce una lista de gaps → esa lista es el input de la siguiente iteración de P3 → P3 produce un prototipo más afinado → P4 hace ship de un agente mejorado → P5 lo testea. La disciplina KV-cache de P1 hace el loop barato — la mayoría del prefijo del agente (tools + system) no cambia entre iteraciones.

---

## Orquestación como composición CLI — el Turtle Corollary (§5)

Una vez que el agente hace ship como CLI (P4), la orquestación multi-agente es simplemente composición de CLIs. No hay distinción arquitectónica entre:

```bash
call_cli gh issue list --label bug
call_cli turtle "revisa este PR para problemas de seguridad"
call_cli leonardo --strategy "descompón esta tarea multi-paso"
```

Los tres son: `parent emite tool call → scaffolding hace dispatch → subprocess corre → output capturado → resultado se convierte en tool-result message en el stream del parent`. El parent no sabe si llamó a un binario Go, un script bash, o un LLM.

### Ventajas del corollary
1. **Backbones heterogéneos**: un supervisor en Claude Opus puede delegar a un worker en DeepSeek y otro en Qwen local.
2. **Aislamiento de procesos**: un hijo que crashea no crashea al padre.
3. **Deployability independiente**: una nueva versión del agente editor reemplaza al anterior sin tocar el orquestador.
4. **Paralelismo vía shell**: `turtle "X" & turtle "Y" & wait` — el mismo primitivo bash de siempre.
5. **Composición con CLIs no-agente**: un orquestador llama a un Turtle que llama a `kubectl` que llama a otro Turtle.
6. **Replayability y auditoría**: cada agente tiene un transcript; el parent referencia a los hijos por invocación.

### Topología Ninja Turtles (multi-agente)

| Agente | Rol | Función |
|--------|-----|---------|
| **Splinter** | Orquestador/master | Descompone la tarea y delega. Decide qué especialista recibe qué subtarea. |
| **Leonardo** | Planificador/estratega | Dado un objetivo bajo-especificado, produce un plan estructurado con dependencias. |
| **Donatello** | Investigador/ingeniero | Opera pipelines RAG, web search, inspección de código, análisis de documentos. Devuelve evidencia con citas. |
| **Michelangelo** | Escritor/comunicador | Produce artifacts de cara al usuario: prosa, código, slides, resúmenes. |
| **Raphael** | Ejecutor | El agente con privilegios de side-effect: writes a ficheros, llamadas API, deployments, acciones irreversibles. |

**Flujo típico**: Splinter recibe la tarea → pide plan a Leonardo → despacha a Donatello para evidencia → pasa evidencia + plan a Michelangelo para borrador → invoca a Raphael para commit/deploy/enviar. Cada paso es una invocación `call_cli` de Splinter; cada hijo es un Turtle CLI con su propia sesión, scaffolding y allow-list.

### Ralph loops (subcase)
El patrón de convergencia-loop expresado como CLI:

```bash
# ralph.sh — convergence loop
goal="$1"; check_cli="$2"; max_iter="${3:-10}"
session=$(uuidgen)
for i in $(seq 1 "$max_iter"); do
    turtle "$session" "haz progreso en: $goal"
    "$check_cli" && { echo "convergió en $i iter"; exit 0; }
done
echo "no convergió en $max_iter iter"; exit 1
```

### Dónde el corollary falla — cuándo usar frameworks
1. **Estado tipado compartido entre agentes** (LangGraph's StateGraph).
2. **Streaming de resultados parciales** a través del árbol de orquestación.
3. **Workflows durables, suspendibles, resumibles** (Temporal, Inngest).
4. **Schemas de handoff tipados** entre agentes.
5. **Observabilidad unificada** del árbol completo (LangSmith, Langfuse).
6. **Presupuestos de profundidad de recursión** — el LLM no se pondrá su propio límite; el scaffolding tiene que hacerlo.

---

## Ejemplo trabajado — AAC (Agent-Assisted Creator) (§6)

El AAC es un agente personalizado para la plataforma educativa LAMB, construido entre marzo y abril de 2026. Asiste a educadores (no ingenieros) en crear, refinar y testear tutores IA dentro de LAMB.

**Mapping a la metodología:**

- **P1**: Los cuatro constraints prácticos (coste, alucinación, contexto, tiempo) fueron presiones de ingeniería reales desde el primer prototipo. La disciplina KV-cache se desarrolló durante el build cuando los costes de tokens revelaron dónde se invalidaba el prefijo.

- **P2**: Function calling conduce cada operación del AAC. El `lamb-cli` se desarrolló en paralelo con el agente como liteshell, exponiendo las operaciones assistant/model/knowledge-base/rubric de LAMB.

- **P3**: Claude Code condujo el primer prototipo del AAC contra la plataforma LAMB en vivo. La sesión de reconocimiento reveló que no existía ningún comando `lamb rubric` aunque los asistentes referenciaban rubrics — el primer gap arquitectónico, descubierto por el acto de construir.

- **P4**: El AAC hace ship como `aac`, un CLI con el Turtle pattern. La arquitectura pasó por tres cristalizaciones durante P4 (HTTP-only → direct-call → HTTP-with-ASGI). **La lección más repetida**: no pongas seguridad en el prompt.

- **P5**: Siete bugs de producción distintos fueron capturados por lo que la metodología llama P5 — un agente de propósito general conduciendo al AAC a través de escenarios y observando trazas de herramientas.

---

## Principios de seguridad (transversales)

1. **Nunca poner seguridad en el prompt** — las instrucciones moldean el comportamiento; el allow-list del scaffolding moldea los resultados.
2. **Allow-list en el scaffolding**, no en el modelo.
3. Credenciales: **keychain del SO o variables de entorno**, nunca strings, nunca en system prompt, nunca en argumentos de herramientas.
4. API keys: **nunca viajan sobre HTTP**.
5. **Minimal dependencies**: un agente construido con esta metodología depende de un SDK de proveedor LLM + las dependencias existentes de tu aplicación. Sin frameworks de agentes = superficie de ataque de cadena de suministro radicalmente menor.
