# Evaluación: Diagrama de casos de uso

## Análisis
El documento cuenta con un apartado específico para el diagrama de casos de uso (Sección 7), aunque la imagen correspondiente no se renderiza en el texto proporcionado. La evaluación se ha realizado cruzando la información disponible en las secciones de actores (Sección 8) y tablas de casos de uso (Sección 9), que constituyen la base textual del modelado.

**Puntos fuertes:**
- Los casos de uso están especificados con un alto nivel de detalle, siguiendo una plantilla estructurada (mencionada como método de Durán y Bernárdez) que incluye precondiciones, flujo normal, excepciones, poscondiciones, métricas de rendimiento, frecuencia e importancia.
- Se identifican y describen los actores del sistema (usuario final, personal de plantación, administradores técnicos y de gestión, y sistemas externos como GPS y pasarela de pago), lo que permite delimitar claramente los límites del sistema.
- La cobertura funcional es completa y coherente con los objetivos del proyecto (rutas sostenibles, plantación de árboles, competencia amistosa y gestión administrativa).

**Puntos débiles / Inconsistencias:**
- **Errores de identificación:** En las tablas de casos de uso, el identificador `CU-011` se repite para tres funcionalidades distintas (`Gestionar usuarios`, `Activar usuarios`, `Desactivar usuarios`), lo que rompe la trazabilidad y contradice el índice. De igual forma, el actor `ACT-004` se asigna erróneamente a tres entidades diferentes (Administrador de gestión, GPS y Cuenta bancaria).
- **Definición de relaciones:** Aunque las tablas son detalladas, no se explicita claramente en el texto si existen relaciones de `<<include>>` o `<<extend>>` entre casos de uso (ej. si "Configurar objetivos" es una extensión de "Ver logros" o un caso independiente), lo que dificulta validar la coherencia global del modelado.
- **Notación gráfica:** Al no estar visible la imagen del diagrama en el documento proporcionado, no es posible verificar visualmente el cumplimiento de la notación UML estándar (límites del sistema, estereotipos, líneas de asociación, generalización de actores, etc.). No obstante, la estructura textual sugiere un enfoque sistemático.

Según la rúbrica, el trabajo se sitúa en el nivel de **7/10**: se evidencia un esfuerzo por definir los casos de uso con detalle y se asume un uso adecuado de la notación por la estructura metodológica aplicada, pero las inconsistencias en la identificación y la falta de claridad en las relaciones entre casos de uso impiden considerar que todos estén "definidos correctamente".

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Corregir la numeración:** Asignar identificadores únicos y consecutivos a cada caso de uso y actor (ej. `CU-011`, `CU-012`, `CU-013` para las funciones de gestión de usuarios; `ACT-004`, `ACT-005`, `ACT-006` para los distintos actores). Esto es fundamental para la trazabilidad y la coherencia con el diagrama.
- **Validar la notación UML:** Asegurar que el diagrama insertado utilice correctamente los elementos gráficos estándar: rectángulo para el límite del sistema, elipses para casos de uso, figuras de palo para actores, y líneas con estereotipos `<<include>>`/`<<extend>>` o flechas de generalización donde corresponda.
- **Explicitar relaciones entre casos de uso:** En las tablas o en una nota al diagrama, justificar qué casos de uso son independientes y cuáles dependen de otros, para que el diagrama refleje fielmente la arquitectura funcional.
- **Revisar coherencia diagrama-tablas:** Verificar que cada elipse del diagrama tenga su tabla correspondiente con el mismo identificador y que no haya funcionalidades duplicadas o solapadas.