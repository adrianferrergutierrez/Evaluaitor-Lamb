# Workflow d'Avaluació - Hito 1: Test 2

## Document Avaluat
- **Fitxer:** `tests/test2/A1.2 Memoria trabajo final.docx`
- **Rúbrica:** `tests/test2/rubrica-hito-1.md`
- **Resultat:** `tests/test2/output/evaluacion/evaluacion_final.md`

---

## Resum del Workflow Seguit

L'avaluació s'ha realitzat seguint el pipeline oficial definit a les skills del projecte `.opencode/skills/`, aplicant les skills: `docx_extract_skill`, `evaluator_skill`, `analyze_skill`, `grade_skill` i `report_skill`.

---

## Fase 0: Conversió DOCX → Markdown (`docx_extract_skill`)

**Objectiu:** Convertir el document Word a Markdown estructurat amb extracció d'imatges.

**Eina utilitzada:** `python-docx` (pandoc no disponible)

**Procés:**
1. Verificació que el fitxer DOCX existeix
2. Creació del directori de sortida: `tests/test2/output/phase0_extract/`
3. Extracció de text amb `python-docx`, preservant l'estructura d'encapçalaments
4. Extracció de taules convertides a format Markdown
5. Extracció d'imatges com a fitxers independents amb referències al Markdown

**Resultat:**
- `contents.md`: 104.309 caràcters
- `img/`: 17 imatges extretes

---

## Fase 1: Importació de Rúbrica Externa (`evaluator_skill`)

**Objectiu:** Convertir la taula Markdown de la rúbrica a configuració YAML compatible.

**Eina utilitzada:** `core/config/rubric_importer.py`

**Procés:**
1. Lectura de `rubrica-hito-1.md` (12 criteris en format taula)
2. Generació automàtica de `configs/rubric_hito1_test2.yaml`
3. Generació de 12 prompts individuals a `prompts/hito1_test2/`
4. Correcció dels paths dels prompts per afegir el prefix `hito1_test2/`

**Resultat:**
- `configs/rubric_hito1_test2.yaml`: Configuració completa amb 12 criteris
- `prompts/hito1_test2/`: 12 fitxers de prompt

---

## Fase 2: Avaluació de Criteris (`analyze_skill` / `evaluator_skill`)

**Objectiu:** Avaluar cada criteri de la rúbrica contra el document Markdown utilitzant LLM.

**Eina utilitzada:** `core/evaluation/criterion_evaluator.py`

**Model:** qwen3.6-plus via DashScope (temperature=0.1, max_tokens=4096)

**Resultat per criteri:**

| Criteri | Puntuació |
|---|---|
| Portada | 7.0/10 |
| Tabla de contenidos | 0.0/10 |
| Estilo del documento | 7.0/10 |
| Objetivos | 7.0/10 |
| Requisitos de información | 7.0/10 |
| Requisitos no funcionales | 10.0/10 |
| Diagrama de casos de uso | 7.0/10 |
| Descripción de actores | 7.0/10 |
| Descripción de casos de uso | 9.0/10 |
| Matriz de rastreabilidad: obj-req | 4.0/10 |
| Matriz de rastreabilidad: req-req | 7.0/10 |
| Ética informática | 7.0/10 |

**Output:** 12 fitxers `eval_*.md` + `scores.json`

---

## Fase 3: Càlcul de Nota Ponderada (`grade_skill`)

**Objectiu:** Calcular la nota final ponderada de forma determinística.

**Eina utilitzada:** `core/grading/grader.py`

**Procés:**
1. Lectura dels 12 fitxers `eval_*.md` amb les avaluacions
2. Extracció automàtica de puntuacions amb `ScoreExtractor`
3. Càlcul de la mitjana ponderada amb els pesos de la rúbrica

**Resultat:**
- **Nota ponderada:** 7.31/10
- **Mitjana aritmètica (x̄):** 6.58/10
- **Nivell de rendiment:** Bueno

---

## Fase 4: Generació d'Informe Final (`report_skill`)

**Objectiu:** Sintetitzar totes les avaluacions en un informe consolidat.

**Eina utilitzada:** `core/evaluation/evaluator.py`

**Procés:**
1. Càrrega de 12 fitxers `eval_*.md`
2. Càrrega de `scores.json` i `rubric_hito1_test2.yaml`
3. Generació de taula de rúbrica amb `RubricGrader`
4. Generació d'informe amb LLM (qwen3.6-plus)

**Resultat:** Informe complet (`evaluacion_final.md`) amb resum executiu, anàlisi per criteris, observacions transversals, recomanacions i conclusions.

---

## Diagrama del Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    PIPELINE D'AVALUACIÓ                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │  FASE 0      │    │  FASE 1      │    │  FASE 2          │  │
│  │  DOCX→MD     │───▶│  Importar    │───▶│  Avaluar         │  │
│  │  (docx_ext)  │    │  Rúbrica     │    │  Criteris        │  │
│  └──────────────┘    └──────────────┘    └──────────────────┘  │
│         │                    │                     │            │
│         ▼                    ▼                     ▼            │
│   contents.md          rubric_hito1_      eval_*.md +          │
│   img/ (17)            test2.yaml         scores.json          │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐                           │
│  │  FASE 3      │    │  FASE 4      │                           │
│  │  Calcular    │───▶│  Generar     │                           │
│  │  Nota        │    │  Informe     │                           │
│  └──────────────┘    └──────────────┘                           │
│         │                    │                                   │
│         ▼                    ▼                                   │
│   7.31/10 (Bueno)     evaluacion_final.md                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Skills Utilitzades

| Skill | Fase | Descripció |
|-------|------|------------|
| `docx_extract_skill.md` | Fase 0 | Conversió DOCX → Markdown + extracció d'imatges |
| `evaluator_skill.md` | Fase 1-2 | Importació de rúbrica i avaluació de criteris |
| `analyze_skill.md` | Fase 2 | Anàlisi amb context (huérfanos, SMART, ISO 25010) |
| `grade_skill.md` | Fase 3 | Càlcul determinístic de nota ponderada |
| `report_skill.md` | Fase 4 | Generació d'informe final consolidat |

---

## Regles Aplicades

- **R1 (Evidència obligatòria):** Cada judici evaluatiu inclou cites textuals, IDs d'elements o descripcions de diagrames.
- **R4 (Càlcul determinístic):** La nota final s'ha calculat exclusivament amb `core/grading/grader.py`.
- **R5 (Format de l'informe):** L'informe inclou taula de rúbrica, resum executiu, anàlisi per criteri, recomanacions i peu de pàgina obligatori.

---

## Limitacions

- **Visió per a diagrames:** Els diagrames UML s'han avaluat sense visió directa de les imatges extretes (requereix model de visió com `qwen-vl-max`).

---

## Canvis realitzats al codi per habilitar totes les skills

Per fer que totes les skills siguin utilitzables sense dependre d'Ollama, s'han fet els següents canvis:

### 1. Mòduls d'extracció → DashScope (Opció A)

- **`core/extraction/objectives.py`**: Canviat backend d'Ollama a `DashScopeClient`. Model per defecte: `qwen3.6-plus`.
- **`core/extraction/requirements.py`**: Idem. Model per defecte: `qwen3.6-plus` (abans `qwen2.5-coder:1.5b`).
- **`core/extraction/use_cases.py`**: Idem. Model per defecte: `qwen3.6-plus`.

Tots tres ara accepten un `client: Optional[DashScopeClient]` com a paràmetre opcional.

### 2. `criterion_evaluator.py` → Nova opció `--full`

S'ha afegit la funció `build_context()` que executa automàticament:
- `extract_objectives()` → Objectius estructurats (OBJ-X)
- `extract_requirements()` → Requisits estructurats (IRQ/NFR)
- `extract_use_cases()` → Casos d'ús (CU-XXX)
- `detect_orphans()` → Detecció de requisits/objectius orfes
- `evaluate_objectives_smart()` → Anàlisi SMART heurístic
- `classify_requirements_iso25010()` → Classificació ISO 25010

El resultat s'injecta al prompt via `--{CONTEXTO}--` abans d'avaluar cada criteri.

### 3. `run_evaluation.py` → Script wrapper

Nou script que orquestra tot el pipeline amb una sola comanda:
```bash
python run_evaluation.py \
  --input <docx> \
  --rubric <rubric.md> \
  --output <output_dir> \
  [--full]
```

---

*Document generat automàticament com a part del procés d'avaluació del Hito 1 - Enginyeria del Software I*

*Nota: Aquest informe és una eina de suport. La qualificació final és responsabilitat exclusiva del professorat.*
