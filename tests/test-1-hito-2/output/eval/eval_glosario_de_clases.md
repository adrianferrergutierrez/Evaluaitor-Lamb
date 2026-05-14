# Evaluación: Glosario de clases

## Análisis
El documento incluye la sección "13. Glosario de clases", estructurada mediante 11 tablas (Tablas 43 a 53) que documentan las clases identificadas en el diagrama de dominio. Cada entrada contiene los campos requeridos: nombre de la clase, descripción, atributos y operaciones. Se cubren todas las entidades del modelo (`Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`), cumpliendo así con el requisito de exhaustividad y explicación del significado.

No obstante, al evaluar el rigor técnico del contenido, se detectan desviaciones importantes respecto a las convenciones de modelado de dominio:
- **Operaciones mal definidas:** En lugar de listar métodos o comportamientos propios de cada clase (ej. `calcularDistancia()`, `registrarPlantacion()`, `validarPago()`), la columna "Operaciones" describe sistemáticamente **relaciones y multiplicidades** entre clases (ej. *"el usuario puede hacer 0 o varias rutas"*, *"la zona puede estar vacía o tener muchos árboles"*). Esto confunde asociaciones estructurales con responsabilidades de comportamiento.
- **Atributos vs. Relaciones:** Algunos campos listados como atributos son en realidad referencias a otras entidades (ej. `Usuario` en la clase `Árbol`, o `Empresa de plantación` en `Mantenimiento`), lo cual no es correcto en un modelo de dominio conceptual.
- **Nomenclatura y abstracción:** La clase `Hacer ruta` utiliza un verbo, lo que indica que modela una acción o caso de uso, no una entidad del dominio. Además, existen inconsistencias en el uso de singular/plural (`Objetivos`, `Donaciones` vs. `Usuario`, `Árbol`).

A pesar de estas imprecisiones conceptuales, el glosario cumple estructuralmente con el criterio al presentar todas las clases, su significado, atributos y operaciones, por lo que se ajusta al nivel de 7/10 de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Corregir la columna "Operaciones":** Sustituir las descripciones de relaciones por métodos reales con signatura clara (nombre, parámetros y tipo de retorno) que reflejen el comportamiento o responsabilidad de la clase dentro del dominio.
- **Revisar atributos:** Asegurar que solo se incluyan propiedades intrínsecas de la entidad. Las relaciones deben representarse mediante asociaciones en el diagrama de clases, no como atributos que referencian a otras clases.
- **Refactorizar nombres de clases:** Cambiar `Hacer ruta` por una entidad de dominio adecuada como `Ruta` o `RegistroDeActividad`. Unificar la nomenclatura en singular para todas las clases.
- **Alinear con el diagrama de dominio:** Verificar que las multiplicidades y roles descritos en el glosario coincidan exactamente con las líneas de asociación del diagrama, manteniendo una separación clara entre estructura (atributos/relaciones) y comportamiento (operaciones).