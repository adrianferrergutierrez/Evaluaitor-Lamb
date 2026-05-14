# Evaluación: Matriz de rastreabilidad: obj-req

## Análisis
El documento presenta la matriz de rastreabilidad objetivos-requisitos en la sección `2.5.1` (Tabla 48). Sin embargo, al contrastarla con el catálogo de requisitos detallado en las tablas individuales del documento, se identifican deficiencias estructurales y de coherencia que impiden considerarla correcta:

1. **Requisitos omitidos:** La matriz no incluye filas para `IRQ-007` (Voluntariado), `IRQ-008` (ONG) ni `CRQ-006` (Restricción de roles), a pesar de estar formalmente definidos en las Tablas 13, 14 y 20.
2. **Falta de asociación explícita:** Filas como `IRQ-006` y `CRQ-005` aparecen completamente vacías en la matriz (sin ninguna marca "X"). No obstante, en sus respectivas tablas de definición (`Tabla 12` y `Tabla 19`) sí se especifican objetivos asociados (`OBJ-005` para IRQ-006 y los cinco objetivos para CRQ-005).
3. **Inconsistencias directas:** Existen contradicciones entre la matriz y las tablas de requisitos. Por ejemplo:
   - `IRQ-001`: La matriz lo asocia a OBJ-001, OBJ-002 y OBJ-004, pero la `Tabla 7` indica OBJ-001, OBJ-002 y OBJ-005.
   - `IRQ-002`: La matriz marca OBJ-002, OBJ-004 y OBJ-005, mientras que la `Tabla 8` solo menciona OBJ-002.
   - `CRQ-003`: La matriz omite OBJ-003, pero la `Tabla 17` lo incluye explícitamente.
4. **Cobertura incompleta:** Debido a las omisiones y celdas vacías, no se garantiza que cada requisito esté justificado por al menos un objetivo, rompiendo el principio fundamental de trazabilidad completa.

La matriz existe y sigue un formato tabular adecuado, pero las omisiones y contradicciones la hacen poco fiable para el seguimiento del proyecto, situándola en el nivel de "no correcta".

## Puntuación
**Puntuación:** 4/10

## Observaciones
- **Completar la matriz:** Añadir las filas correspondientes a `IRQ-007`, `IRQ-008` y `CRQ-006` para que refleje la totalidad del catálogo de requisitos.
- **Corregir inconsistencias:** Revisar celda por celda y asegurar que las marcas "X" coincidan exactamente con el campo `Objetivos asociados` de cada tabla de requisito individual.
- **Eliminar celdas vacías:** Garantizar que cada requisito tenga al menos una asociación con un objetivo. Si un requisito no aporta a ningún objetivo, debe justificarse su inclusión o eliminarse del catálogo.
- **Validación cruzada:** Implementar un proceso de revisión donde la matriz se genere o actualice automáticamente a partir de las tablas de requisitos, evitando errores manuales de transcripción.
- **Separación de niveles (opcional):** Considerar mantener una matriz `Objetivos ↔ Requisitos` y otra `Requisitos ↔ Casos de Uso` para mejorar la legibilidad y el mantenimiento de la trazabilidad.