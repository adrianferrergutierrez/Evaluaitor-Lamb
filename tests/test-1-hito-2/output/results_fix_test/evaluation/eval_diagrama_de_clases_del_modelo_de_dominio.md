# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye el diagrama de clases del modelo de dominio (Imagen 31) y su correspondiente glosario (Tablas 43 a 53). A continuación, se evalúa su calidad conceptual y notacional frente a la rúbrica y la especificación de requisitos:

**Aspectos positivos:**
- **Notación UML correcta:** Se utiliza la sintaxis estándar de diagramas de clases (compartimentos para nombre y atributos, líneas de asociación, multiplicidades, estereotipo `<<enumeration>>` para `Tipo Transporte`).
- **Identificación de entidades principales:** El modelo captura los conceptos clave del dominio: `Usuario`, `Objetivo`, `Donación`, `Empresa de plantación`, `Zona`, `Árbol`, `Ruta Predeterminada`, `Ruta no predeterminada`, `Tipo Transporte` y `Mantenimiento`.
- **Atributos coherentes:** La mayoría de los atributos reflejan adecuadamente la información del dominio (ej. `Usuario` con nombre/correo, `Objetivo` con descripción y estado booleano, `Zona` con ubicación y hectáreas).

**Deficiencias y errores conceptuales:**
- **Falta de cobertura de requisitos clave:** El objetivo `OBJ-003 Competencia amistosa` y el caso de uso `CU-005 Competir con amigos` son centrales en la aplicación, pero el modelo de dominio no incluye ninguna clase `Amistad`, `Amigo`, ni una auto-asociación en `Usuario` para representar relaciones de amistad. Esto deja un hueco importante en la especificación.
- **Relaciones conceptualmente incorrectas:**
  - `Ruta Predeterminada` y `Ruta no predeterminada` están unidas por una asociación muchos-a-muchos llamada `"Red"`. Conceptualmente, ambas deberían ser especializaciones (herencia/generalización) de una clase base `Ruta`, no entidades relacionadas entre sí.
  - `Empresa de plantación` tiene una asociación `"Recibe"` con `Ruta Predeterminada` (0..1 a 0..*). En el dominio, las empresas gestionan plantaciones y zonas, no reciben rutas de usuarios. Esta relación carece de sentido semántico.
  - La clase `Árbol` incluye un atributo `Cantidad: Integer`. Si `Árbol` representa una entidad individual, no debería tener un atributo de cantidad; si representa un conjunto, debería modelarse mediante una asociación con `Usuario` o `Zona`, o crearse una clase `Lote/Plantación`.
  - `Mantenimiento` se modela con un atributo booleano `Mantenimiento a realizar`, lo cual es más propio de un estado o una operación que de un concepto de dominio. Debería asociarse a `Zona` o `Árbol` con atributos como fecha, tipo o estado.
- **Nivel de abstracción:** Aunque se trata de un modelo de dominio (conceptual), el glosario incluye operaciones detalladas (ej. `Enviar donación`, `Crear ruta predeterminada`), lo cual es más propio de un modelo de diseño software que de un modelo de dominio puro.

**Conclusión frente a la rúbrica:**
El diagrama utiliza correctamente la notación UML y plantea una estructura base identificable, pero presenta errores conceptuales en las relaciones, omite clases necesarias para cubrir objetivos funcionales clave (competencia/amistades) y modela algunas entidades de forma inconsistente con el dominio real. Esto se ajusta al nivel de **7/10**: notación adecuada, pero modelo incompleto y con relaciones/clases que no reflejan fielmente la especificación de requisitos.

## Puntuación
**Puntuación:** 7/10

## Observaciones
1. **Modelar la competencia/amistad:** Añadir una clase `Amistad` (con atributos como fecha de creación o estado) o una auto-asociación en `Usuario` (ej. `amigos 0..*`) para cubrir el objetivo `OBJ-003` y el caso de uso `CU-005`.
2. **Corregir la jerarquía de rutas:** Reemplazar la asociación `"Red"` entre `Ruta Predeterminada` y `Ruta no predeterminada` por una relación de generalización (`<<inheritance>>`) hacia una clase abstracta `Ruta` que contenga los atributos comunes (origen, destino, tipo de transporte, distancia, etc.).
3. **Revisar asociaciones sin sentido de dominio:** Eliminar o redefinir la relación `"Recibe"` entre `Empresa de plantación` y `Ruta Predeterminada`. Las empresas deberían asociarse a `Zona`, `Árbol` y `Mantenimiento`, no a rutas de usuarios.
4. **Refinar `Árbol` y `Mantenimiento`:** 
   - `Árbol` debe representar una instancia única. Si se necesita contar árboles, usar una asociación con multiplicidad o una clase `RegistroPlantación`.
   - `Mantenimiento` debe modelarse como una entidad con atributos como `fecha`, `tipo`, `estado` o `observaciones`, asociada a `Zona` o `Árbol`.
5. **Separar modelo de dominio de diseño:** En el glosario, limitar las "Operaciones" a comportamientos conceptuales de alto nivel o eliminarlas, ya que el modelo de dominio debe centrarse en conceptos, atributos y relaciones, no en responsabilidades de implementación software.