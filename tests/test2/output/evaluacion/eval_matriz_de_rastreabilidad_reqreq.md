# Evaluación: Matriz de rastreabilidad: req-req

## Análisis
El documento presenta la matriz de rastreabilidad de requisitos con requisitos en la sección **2.5.2 (Tabla 49)**. La estructura es una tabla cuadrada que cruza los requisitos de información (IRQ), restricciones (CRQ), no funcionales (NFR) y casos de uso (CU), utilizando una “X” para indicar relaciones de dependencia.

Al contrastar la matriz con el catálogo completo definido en el documento, se identifican las siguientes deficiencias:
- **Requisitos omitidos**: `IRQ-008 (ONG)` (Tabla 14) y `CRQ-006 (Restricción de roles)` (Tabla 20) están correctamente definidos en el catálogo, pero **no aparecen** ni en las filas ni en las columnas de la matriz.
- **Mezcla de artefactos**: La matriz incluye los casos de uso (CU-001 a CU-020) junto con los requisitos. Aunque es una práctica común en entornos académicos, técnicamente la convierte en una matriz híbrida (req-req + req-CU) en lugar de una matriz estricta de requisitos con requisitos.
- **Coherencia de relaciones**: Las dependencias marcadas son generalmente plausibles (los NFR actúan como requisitos transversales y `IRQ-001` funciona como nodo central). No obstante, la ausencia de los requisitos mencionados rompe la cobertura completa exigida por una trazabilidad rigurosa.

Dado que la matriz existe y está estructurada, pero no incluye la totalidad de los requisitos definidos en el documento, se ajusta exactamente al nivel de la rúbrica correspondiente a una puntuación de 7/10.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Completar la matriz**: Añadir `IRQ-008` y `CRQ-006` como filas y columnas, y establecer sus relaciones de dependencia con el resto de requisitos (especialmente con `IRQ-001`, `IRQ-002`, `CRQ-005` y los NFR).
- **Separar trazabilidades**: Crear dos matrices diferenciadas: una estrictamente **req-req** (IRQ, CRQ, NFR) y otra **req-CU**. Esto mejora la claridad, facilita el mantenimiento y se alinea con estándares de ingeniería de requisitos.
- **Estandarizar marcado**: Unificar el símbolo de relación (usar exclusivamente `X` o `1`) para evitar inconsistencias visuales y posibles errores de interpretación.
- **Validar bidireccionalidad**: Revisar que las dependencias sean coherentes en ambas direcciones o justificar explícitamente cuando la relación sea unidireccional (ej. un requisito de restricción que afecta a un requisito de información, pero no viceversa).