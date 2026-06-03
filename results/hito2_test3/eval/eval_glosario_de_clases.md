# Evaluación: Glosario de clases

## Análisis
El glosario de clases se encuentra documentado en las Tablas 43 a 53 del documento. Se identifican y describen 11 clases correspondientes al modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. Cada tabla incluye los campos requeridos: descripción de la clase, atributos (con indicación de tipo de dato) y operaciones.

El documento cumple con la estructura solicitada y cubre todas las clases derivadas del diagrama de clases. Las descripciones son claras y contextualizadas al dominio de la aplicación. Sin embargo, se observan imprecisiones conceptuales en el apartado de "Operaciones": en la mayoría de las tablas, este campo describe en realidad *asociaciones y multiplicidades* entre clases (ej. `"Usuario: el usuario puede hacer una ruta 0 o muchas veces"`) en lugar de métodos o responsabilidades de comportamiento propias de la clase. Asimismo, la clase `Hacer ruta` modela conceptualmente un caso de uso o una acción, no una entidad del dominio, lo cual desvía ligeramente la pureza del modelo de dominio.

A pesar de estas observaciones técnicas, el glosario presenta todas las clases, explica su significado y detalla atributos y operaciones, ajustándose al nivel de completitud definido en la rúbrica para la puntuación de 7/10.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Diferenciar operaciones de asociaciones:** Revisar el campo "Operaciones" para que refleje métodos reales de la clase (ej. `crearRuta()`, `actualizarEstado()`, `registrarDonación()`) en lugar de describir relaciones o cardinalidades con otras clases.
- **Revisar la clase "Hacer ruta":** Esta clase representa una acción/caso de uso. Se recomienda eliminarla como entidad de dominio y trasladar su lógica como un método de la clase `Usuario` o `Ruta`.
- **Estandarizar nomenclatura:** Aplicar notación PascalCase sin espacios para los nombres de clases (ej. `EmpresaPlantacion`, `RutaPredeterminada`, `TipoTransporte`) para alinearse con las convenciones de UML y programación orientada a objetos.
- **Refinar atributos:** Asegurar que los atributos listados sean propiedades intrínsecas de la clase. Por ejemplo, en `Árbol`, el atributo `Usuario` parece ser una relación; debería modelarse como una asociación en el diagrama y no como un atributo de tipo `String`.