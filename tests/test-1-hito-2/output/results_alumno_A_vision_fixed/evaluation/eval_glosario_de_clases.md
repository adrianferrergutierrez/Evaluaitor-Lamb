# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **13. Glosario de clases**, el cual se desarrolla mediante las Tablas 43 a 53. En estas tablas se documentan 11 clases correspondientes al modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. 

Cada clase cuenta con los campos estructurales solicitados:
- **Descripción:** Explica de forma clara y contextualizada el significado de la clase dentro del dominio del problema.
- **Atributos:** Se listan con su nombre y tipo de dato (String, Boolean, Float, Integer, etc.), cumpliendo con el requisito de documentación.
- **Operaciones:** Se incluyen para todas las clases.

Sin embargo, al revisar el contenido del campo **Operaciones**, se observa un error conceptual recurrente: en lugar de definir métodos o comportamientos propios de la clase (ej. `calcularDistancia()`, `validarDonación()`, `actualizarEstado()`), se han descrito principalmente **relaciones de asociación y sus multiplicidades** con otras clases (ej. *"el usuario puede hacer una ruta 0 o muchas veces"*, *"planta uno o varios árboles"*, *"recibe 0 o varias donaciones"*). Aunque formalmente el campo está rellenado, conceptualmente confunde operaciones con relaciones, lo cual impide considerar que los métodos estén "explicados correctamente" según la rúbrica. Aun así, la cobertura es completa y la estructura base está bien implementada, situándose en el nivel intermedio-alto de la escala.

## Puntuación
**Puntuación:** 7/10

## Observaciones
1. **Corregir el campo "Operaciones":** Sustituir las descripciones de asociaciones/multiplicidades por verdaderos métodos o comportamientos que la clase puede ejecutar o recibir (ej. en `Ruta predeterminada`: `calcularTiempoEstimado()`, `editarRuta()`; en `Empresa de plantación`: `registrarPlantación()`, `notificarMantenimiento()`).
2. **Separar relaciones de operaciones:** Las asociaciones y cardinalidades deben documentarse en el diagrama de clases o en una tabla específica de relaciones, no en el glosario de operaciones.
3. **Revisar nomenclatura y granularidad:** Algunas clases como `Hacer ruta` representan acciones o casos de uso, no entidades del dominio. Sería más adecuado modelar una clase `Ruta` con un atributo `tipo` (predeterminada/no predeterminada) o `estado`. Además, unificar el singular/plural en los nombres (`Donaciones` → `Donación`, `Objetivos` → `Objetivo`) mejorará la coherencia del modelo.
4. **Completar tipos de datos:** En atributos como `Método de transporte` o `Transporte`, se indica `Tipo de transporte` como tipo; es recomendable especificar si es un `enum` o `String` con valores restringidos para mayor precisión técnica.