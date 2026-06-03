# Evaluación: Glosario de clases

## Análisis
El documento incluye la sección **13. Glosario de clases**, que se materializa en las Tablas 43 a 53. En total se documentan 11 clases del modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. 

Cada tabla sigue una estructura uniforme y contiene los campos requeridos por la rúbrica:
- **Descripción:** Se explica el significado y propósito de cada clase en el contexto del dominio.
- **Atributos:** Se listan los atributos principales junto con su tipo de dato (String, Boolean, Float, Integer, etc.).
- **Operaciones:** Se incluyen las operaciones/métodos asociados a cada clase.

El glosario cubre todas las clases presentes en el diagrama de clases referenciado (sección 12) y mantiene coherencia con los requisitos y casos de uso descritos previamente. Cumple con los criterios de completitud y estructura exigidos para el nivel de 7/10. No obstante, se observa una imprecisión conceptual recurrente: en varias tablas (44, 45, 49, 51, 52, 53) el campo "Operaciones" se utiliza para describir **relaciones y cardinalidades** entre clases (ej. *"Usuario: el usuario puede hacer una ruta 0 o muchas veces"*) en lugar de métodos funcionales o comportamientos propios de la clase. Además, algunos nombres de clase (como `Hacer ruta`) suenan más a casos de uso que a entidades de dominio, y ciertos atributos podrían refinarse para reflejar mejor las relaciones (ej. `Usuario (String)` en la clase `Árbol` debería ser una referencia o identificador). Aun así, el trabajo es completo, está bien organizado y cumple con los requisitos mínimos del nivel intermedio-alto de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Separar operaciones de relaciones:** Se recomienda crear un campo adicional para "Relaciones/Asociaciones" donde se especifiquen las clases vinculadas y su cardinalidad (1..*, 0..1, etc.), reservando "Operaciones" exclusivamente para métodos o comportamientos funcionales (ej. `calcularDistancia()`, `registrarDonación()`, `actualizarEstado()`).
- **Refinar nomenclatura de clases:** Nombres como `Hacer ruta` o `Objetivos` (en plural) no siguen las convenciones típicas de modelado de dominio. Se sugiere usar sustantivos en singular y abstractos cuando corresponda (ej. `Ruta`, `Objetivo`, `RegistroDeRuta`).
- **Tipado y referencias:** En atributos que representan vínculos (como `Usuario` en la clase `Árbol` o `Empresa de plantación` en `Mantenimiento`), es preferible indicar que son referencias a otras clases o IDs, en lugar de tipos primitivos como `String`.
- **Consistencia en enumeraciones:** La clase `Tipo de transporte` está correctamente identificada como enumeración, pero podría listarse explícitamente sus valores permitidos en el glosario para mayor claridad.
Implementar estas mejoras elevaría la precisión técnica y alinearía el glosario con estándares profesionales de ingeniería del software, acercándolo al nivel máximo de la rúbrica.