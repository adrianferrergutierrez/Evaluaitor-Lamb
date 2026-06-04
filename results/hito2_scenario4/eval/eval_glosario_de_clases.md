# Evaluación: Glosario de clases

## Análisis
El documento incluye la sección **13. Glosario de clases**, que se materializa en las **Tablas 43 a 53**. En estas tablas se documentan 11 clases correspondientes al modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. 

Cada tabla sigue una estructura consistente que incluye:
- **Descripción:** Explica claramente el significado y propósito de cada clase dentro del dominio del problema.
- **Atributos:** Se listan con sus tipos de datos correspondientes (String, Boolean, Float, Integer, etc.). En casos como `Hacer ruta` y `Tipo de transporte` se indica explícitamente que no poseen atributos.
- **Operaciones:** Se detallan las responsabilidades y comportamientos principales de cada clase.

El glosario cubre todas las clases identificadas en el diagrama de clases del modelo de dominio, cumpliendo con los requisitos de descripción, significado, atributos y métodos/operaciones principales. Sin embargo, las operaciones se presentan de forma narrativa y descriptiva (ej. *"Enviar donación: el usuario puede enviar 0 o varias donaciones a una empresa de plantación"*) en lugar de utilizar firmas de métodos formales (ej. `registrarDonacion(cantidad: Float): void`). Además, algunos nombres de clases no siguen la convención estándar de sustantivos en singular (`Objetivos`, `Donaciones`, `Hacer ruta`), lo cual es una desviación menor de las buenas prácticas de UML, pero no invalida la completitud del apartado. Por tanto, el trabajo se ajusta exactamente al nivel de 7/10 definido en la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Formato de operaciones:** Se recomienda transformar las descripciones narrativas de las operaciones en firmas de métodos formales (nombre, parámetros con tipo, y tipo de retorno) para alinearse con el estándar UML y facilitar la transición a la fase de diseño/implementación.
- **Nomenclatura de clases:** Aplicar la convención de nombrar las clases con sustantivos en singular y en PascalCase (ej. `Objetivo` en lugar de `Objetivos`, `Donación` en lugar de `Donaciones`, `RegistroDeRuta` o `Ruta` en lugar de `Hacer ruta`).
- **Consistencia con el diagrama:** Verificar que las multiplicidades y relaciones descritas en las operaciones coincidan exactamente con las asociaciones y cardinalidades representadas en el diagrama de clases (Sección 12 / Imagen 1).
- **Documentación de tipos personalizados:** Si `Tipo de transporte` se usa como tipo de dato en otras clases, sería útil añadir una breve nota o referencia a su definición como enumeración (`enum`) para mayor claridad técnica.