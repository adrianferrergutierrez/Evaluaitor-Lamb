# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **13. Glosario de clases**, compuesto por 11 tablas (Tabla 43 a Tabla 53) que corresponden a las entidades del modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. Cada tabla mantiene una estructura uniforme con los campos: Clase, Descripción, Atributos y Operaciones.

- **Descripción/Meaning:** Todas las clases cuentan con una explicación clara de su rol dentro del dominio del problema (ej. *"Representa a las personas que utilizan la aplicación"*, *"Lugares en los que están plantados los árboles conseguidos por los usuarios"*).
- **Atributos:** Se detallan los atributos principales junto con su tipo de dato (`String`, `Boolean`, `Float`, `Integer`, etc.). Aunque en algunos casos son básicos, cumplen con el requisito de identificación de propiedades estructurales.
- **Operaciones/Métodos:** Se incluyen en todas las tablas. No obstante, se evidencia una confusión conceptual típica en etapas iniciales de modelado: en lugar de definir comportamientos o métodos propios de la clase (ej. `calcularDistancia()`, `registrarDonación()`), se describen **relaciones de asociación y multiplicidades** con otras clases (ej. en *Hacer ruta*: *"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."*). Además, clases como `Hacer ruta` poseen un nombre más propio de un caso de uso que de una entidad estructural del dominio.

En conjunto, el glosario cumple con los requisitos estructurales exigidos por la rúbrica: se han descrito todas las clases, se ha explicado su significado y se han detallado atributos y operaciones principales. Por ello, se ajusta al nivel de **7/10**. No alcanza la máxima puntuación debido a la imprecisión técnica en la definición de operaciones (confundidas con asociaciones) y a la inclusión de clases con naturaleza conductual en lugar de estructural.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Diferenciar operaciones de asociaciones:** En un glosario de clases del modelo de dominio, el campo "Operaciones" debe reflejar comportamientos o métodos propios de la clase (ej. `validarCredenciales()`, `actualizarEstado()`, `calcularProgreso()`). Las relaciones, cardinalidades y asociaciones deben quedar reflejadas exclusivamente en el diagrama de clases, no en las tablas del glosario.
- **Revisar la nomenclatura de las clases:** Evitar nombres que describan acciones o flujos (como `Hacer ruta`). Sustituirlos por entidades del dominio como `Ruta`, `RegistroDeActividad` o `SesionDeRuta`.
- **Completar atributos clave:** Algunas clases podrían enriquecerse con atributos relevantes para el dominio (ej. en `Árbol`: `especie`, `fechaPlantacion`, `estado`; en `Donaciones`: `fecha`, `metodoPago`, `estadoTransaccion`; en `Mantenimiento`: `fechaProgramada`, `tipoIntervencion`).
- **Unificar notación de tipos de datos:** Mantener consistencia en la declaración de tipos (ej. usar `String`, `Integer`, `Boolean` de forma estandarizada y evitar mezclar tipo y semántica en la misma celda).
- Con estas correcciones, el glosario ganaría rigor técnico, se alinearía con las buenas prácticas de modelado orientado a objetos y podría alcanzar la máxima calificación.