# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **13. Glosario de clases** (Tablas 43 a 53), donde se detallan 11 clases correspondientes al diagrama de clases del modelo de dominio. Cada clase presenta una estructura uniforme con los campos: *Descripción*, *Atributos* y *Operaciones*. 

- **Cobertura y significado:** Se han descrito todas las clases identificadas en el modelo de dominio y cada una cuenta con una descripción clara que explica su propósito dentro del sistema (ej. `Usuario`, `Ruta predeterminada`, `Empresa de plantación`, `Zona`).
- **Atributos:** Se listan correctamente con sus tipos de datos correspondientes (`String`, `Boolean`, `Float`, `Integer`, enumeraciones), lo cual es adecuado para un glosario de dominio.
- **Operaciones (Métodos):** Se detecta una **desviación metodológica importante**. En lugar de definir operaciones o métodos que representen el comportamiento o responsabilidades de la clase (ej. `calcularDistancia()`, `registrarPlantación()`, `validarPago()`), las tablas describen **asociaciones, multiplicidades y flujos de casos de uso**. Por ejemplo, en la clase `Hacer ruta` se indica: *"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."*, y en `Zona`: *"la zona... puede estar vacía todavía, o tener ya muchos registrados en ella"*. Esto confunde la estructura relacional del diagrama con el comportamiento de la clase.
- **Nomenclatura:** Algunas clases utilizan verbos o plurales (`Hacer ruta`, `Objetivos`, `Donaciones`), lo cual no sigue la convención estándar de modelado de dominio (deben ser sustantivos en singular que representen conceptos o entidades).

En conjunto, el glosario cumple con la estructura requerida y cubre todas las clases, pero la incorrecta formulación de las operaciones impide alcanzar el nivel de "explicación correcta" exigido para la puntuación de 7/10 según la rúbrica.

## Puntuación
**Puntuación:** 6/10

## Observaciones
- **Corregir el campo "Operaciones":** Deben redefinirse como métodos reales que describan el comportamiento o responsabilidades de la clase, preferiblemente con una firma simplificada o una descripción funcional (ej. `registrarRuta()`, `actualizarEstado()`, `calcularProgreso()`). Las relaciones y multiplicidades deben quedar exclusivamente en el diagrama de clases, no en el glosario.
- **Ajustar la nomenclatura:** Renombrar las clases a sustantivos en singular (`Ruta` en lugar de `Hacer ruta`, `Objetivo` en lugar de `Objetivos`, `Donación` en lugar de `Donaciones`) para alinearse con las buenas prácticas de UML y modelado de dominio.
- **Revisar coherencia con el diagrama:** Asegurar que los atributos y métodos listados reflejen fielmente las responsabilidades identificadas en el modelo de dominio y no repitan lógica de casos de uso.
- **Tipado de atributos:** Verificar que todos los atributos tengan tipos de datos consistentes y evitar mezclar conceptos de dominio con detalles de implementación prematura o lógica de interfaz.