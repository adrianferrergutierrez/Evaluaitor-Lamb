# Evaluación: Glosario de clases

## Análisis
El documento incluye el glosario de clases, localizado en las Tablas 43 a 53, donde se detallan 11 clases correspondientes al modelo de dominio (`Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`). Cada entrada cumple con la estructura solicitada: contiene una **descripción** que explica el significado y propósito de la clase, una lista de **atributos** con sus tipos de datos, y una sección de **operaciones** (métodos) que detalla las funcionalidades asociadas. Esto satisface explícitamente el nivel de 7/10 de la rúbrica, ya que se han descrito todas las clases del diagrama y se han incluido su significado, atributos y métodos principales.

No obstante, se identifican ciertas imprecisiones conceptuales propias del modelado de dominio que impiden alcanzar la máxima puntuación:
- Clases como `Hacer ruta` representan acciones o casos de uso, no entidades conceptuales del dominio.
- Las "operaciones" se redactan en lenguaje natural con multiplicidades (ej. *"el usuario puede enviar 0 o varias donaciones"*) en lugar de firmas de métodos típicas de un glosario técnico.
- Algunos atributos (como `Usuario (String)` en la clase `Árbol` o `Empresa de plantación` en `Mantenimiento`) modelan relaciones que deberían reflejarse como asociaciones en el diagrama, no como campos de tipo primitivo.
- El glosario no está ubicado directamente bajo el epígrafe `13. Glosario de clases`, sino tras las imágenes, lo que dificulta ligeramente la trazabilidad.

A pesar de estas observaciones, el apartado está completo, bien estructurado y cumple con los requisitos mínimos y descriptivos establecidos en la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Separar entidades de acciones:** Revisar el modelo de dominio para eliminar clases que representan comportamientos o casos de uso (ej. `Hacer ruta`) y sustituirlas por entidades reales o moverlas a la capa de control/servicio.
- **Formalizar las operaciones:** Redactar los métodos con notación técnica estándar (ej. `registrarDonacion(monto: Float): Boolean`) en lugar de descripciones narrativas con multiplicidades.
- **Corregir atributos vs. asociaciones:** Los campos que hacen referencia a otras clases (ej. `Usuario` en `Árbol`) deben eliminarse como atributos y representarse exclusivamente como relaciones en el diagrama de clases.
- **Ubicación y formato:** Colocar las tablas del glosario inmediatamente después del título `13. Glosario de clases` para mantener la coherencia estructural del documento y facilitar la revisión.