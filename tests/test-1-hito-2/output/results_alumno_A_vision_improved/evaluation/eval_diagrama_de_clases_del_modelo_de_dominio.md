# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye un glosario de clases (Sección 13, Tablas 43-53) que describe el modelo de dominio, ya que las imágenes del diagrama no son accesibles en el texto proporcionado. A partir de esta descripción y de la memoria técnica, se identifican los siguientes aspectos clave:

1. **Enfoque no conceptual:** El modelo confunde conceptos del dominio del problema con funcionalidades del sistema o casos de uso. Por ejemplo, la clase `Hacer ruta` (Tabla 44) es una acción verbal, no una entidad del dominio. En un modelo de dominio conceptual solo deben aparecer sustantivos que representen elementos del mundo real (ej. `Ruta`, `Registro`, `Usuario`).
2. **Notación y convenciones UML incorrectas:** 
   - Los nombres de clase están en plural (`Objetivos`, `Donaciones`), lo cual viola la convención UML estándar (deben ser singulares).
   - El campo "Operaciones" describe flujos de casos de uso y comportamientos del sistema (`Enviar donación`, `Competir`, `Hacer una ruta`) en lugar de responsabilidades o métodos propios de la clase. Esto indica una mezcla entre modelo de dominio y modelo de diseño/implementación.
   - Las relaciones y multiplicidades no se modelan como asociaciones UML, sino que se describen textualmente dentro de las operaciones, lo que impide una representación gráfica clara y estandarizada.
3. **Cobertura vs. Requisitos:** Aunque se identifican entidades relevantes (`Usuario`, `Ruta predeterminada`, `Árbol`, `Empresa de plantación`, `Zona`, `Mantenimiento`), faltan conceptos implícitos en los requisitos funcionales e información, como `Amistad`/`RelaciónSocial` (para la competencia amistosa), `Historial` (mencionado en IRQ-002/003) o `Transacción`/`Pago` (para las donaciones).
4. **Autodiagnóstico del equipo:** En la Sección 3.5, el grupo reconoce explícitamente: *"Nos costó bastante identificar las clases correctas, ya que decidir qué objetos deberían ser clases y qué relaciones debían existir entre ellas fue todo un reto..."*, lo que corrobora las dificultades conceptuales reflejadas en el entregable.

En conjunto, el trabajo presenta una estructura que intenta cubrir los requisitos, pero no se ha elaborado desde una perspectiva conceptual adecuada y la notación/modelado de relaciones es deficiente, alineándose con el nivel más bajo de la rúbrica que reconoce la existencia del artefacto pero señala fallos fundamentales en su enfoque y notación.

## Puntuación
**Puntuación:** 2/10

## Observaciones
- **Eliminar clases de acción:** Sustituir `Hacer ruta` por entidades conceptuales como `Ruta` o `RegistroDeActividad`. Los verbos pertenecen a los casos de uso, no al modelo de dominio.
- **Corregir nomenclatura:** Utilizar nombres en singular para todas las clases (`Objetivo`, `Donación`, `Usuario`, etc.).
- **Separar dominio de diseño:** Retirar las operaciones de tipo "caso de uso" del modelo de dominio. Un modelo conceptual debe centrarse en atributos y asociaciones, no en flujos de interacción con el sistema.
- **Modelar relaciones explícitamente:** Definir asociaciones con nombres, roles y multiplicidades claras (ej. `Usuario` 1..* `Ruta`, `Usuario` *..* `Amigo`, `Empresa` 1..* `Árbol`).
- **Completar conceptos faltantes:** Incorporar clases como `Amistad`, `HistorialDeRutas` o `Transacción` para reflejar fielmente los requisitos de competencia, seguimiento y pagos.
- **Revisar guías de modelado conceptual:** Consultar referencias sobre la diferencia entre modelo de dominio (espacio del problema) y modelo de diseño (espacio de la solución) para evitar mezclar responsabilidades de interfaz/sistema con entidades del negocio.