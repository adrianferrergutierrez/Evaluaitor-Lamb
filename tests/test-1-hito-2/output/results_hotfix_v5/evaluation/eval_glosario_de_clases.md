# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **"13. Glosario de clases"** (Tablas 43 a 53), donde se documentan 11 clases/entidades del modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. Cada tabla cumple con la estructura solicitada, proporcionando una **descripción** del significado de la clase, un listado de sus **atributos** (con tipos de datos como `String`, `Boolean`, `Float`, `Integer`) y un apartado de **operaciones**. 

Se supera el nivel de 3/10 porque sí se incluyen explícitamente los atributos y un campo dedicado a las operaciones para todas las clases identificadas. No obstante, se detecta una **confusión conceptual recurrente** en el campo "Operaciones": en varias clases (ej. `Hacer ruta`, `Ruta predeterminada`, `Mantenimiento`, `Empresa de plantación`, `Zona`), lo que se describe no son métodos o comportamientos ejecutables, sino **relaciones de asociación o cardinalidades** con otras clases (ej. *"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."* o *"Zona: la zona en la que se plantan los árboles puede estar vacía..."*). En UML, las operaciones deben reflejar el comportamiento interno de la clase (métodos), mientras que las asociaciones se representan gráficamente en el diagrama de clases. Esta imprecisión impide alcanzar la máxima puntuación, aunque el trabajo cumple estructuralmente con los requisitos del nivel 7/10.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Diferenciar operaciones de asociaciones:** Revisar el campo "Operaciones" y sustituir las descripciones de relaciones por métodos reales que la clase debe ejecutar (ej. `calcularDistancia(): Float`, `registrarDonación(cantidad: Float): Boolean`, `actualizarEstado(): void`).
- **Notación UML estándar:** Formalizar las operaciones usando la sintaxis `nombreMétodo(parámetros): tipoRetorno` y especificar visibilidad (`+`, `-`, `#`) si es requerido por la asignatura.
- **Revisión de entidades vs. acciones:** Clases como `Hacer ruta` o `Mantenimiento` tienen un carácter más procedimental (propio de casos de uso o servicios) que de entidad de dominio. Si se mantienen, deben dotarse de atributos y métodos propios de una clase; de lo contrario, considerar su eliminación o transformación en clases de control/servicio.
- **Consistencia en tipos de datos:** Unificar la nomenclatura de tipos (ej. usar `String` o `Texto`, `Boolean` o `Booleano`) y asegurar que todos los atributos tengan un tipo definido.
Con estas correcciones, el glosario se alineará perfectamente con las buenas prácticas de modelado orientado a objetos y alcanzaría el nivel de excelencia.