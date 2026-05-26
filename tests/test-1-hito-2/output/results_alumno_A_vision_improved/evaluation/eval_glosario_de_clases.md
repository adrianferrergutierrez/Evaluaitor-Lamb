# Evaluación: Glosario de clases

## Análisis
El documento incluye el glosario de clases en las **Tablas 43 a 53**, donde se documentan 11 clases derivadas del modelo de dominio. Cada tabla sigue una estructura uniforme que incluye: nombre de la clase, descripción, atributos y operaciones. Sin embargo, al evaluar el contenido técnico frente a los estándares de modelado orientado a objetos y la rúbrica proporcionada, se identifican las siguientes evidencias:

1. **Descripción y significado:** Todas las clases cuentan con una descripción clara de su propósito dentro del dominio (ej. Tabla 43 `Usuario`, Tabla 49 `Árbol`, Tabla 53 `Zona`). Este aspecto cumple con el requisito básico de explicar el significado de cada clase.
2. **Atributos:** Se listan atributos con su tipo de dato en todas las tablas. No obstante, algunos presentan inconsistencias conceptuales o están incompletos respecto a los requisitos de información definidos previamente. Por ejemplo, la clase `Árbol` (Tabla 49) solo incluye `Usuario (String)` y `Cantidad (Integer)`, omitiendo atributos esenciales como especie, estado de crecimiento, coordenadas o fecha de plantación. Asimismo, la clase `Usuario` (Tabla 43) omite la contraseña y el nombre de usuario, detallados en el IRQ-001.
3. **Métodos/Operaciones:** Este es el punto crítico. El campo `Operaciones` **no contiene métodos reales** de la clase (como `registrar()`, `calcularDistancia()`, `actualizarEstado()`, etc.). En su lugar, se describen **relaciones, multiplicidades o flujos de casos de uso**. Por ejemplo:
   - Tabla 44 (`Hacer ruta`): `Usuario: el usuario puede hacer una ruta 0 o muchas veces...`
   - Tabla 51 (`Mantenimiento`): `Zona: Un mantenimiento en específico se realiza en una zona que lo requiera.`
   - Tabla 52 (`Empresa de plantación`): `Árbol: planta uno o varios árboles`
   Esta confusión entre operaciones (comportamiento/métodos) y asociaciones (relaciones estructurales) impide que el glosario cumpla con el nivel de corrección técnica exigido.
4. **Nomenclatura de clases:** La clase `Hacer ruta` (Tabla 44) utiliza un verbo, lo cual es incorrecto en un modelo de dominio donde las clases deben representar conceptos o entidades (sustantivos). Debería denominarse simplemente `Ruta` o `RegistroDeRuta`.

En conclusión, aunque el glosario está estructuralmente completo y describe el significado de todas las clases, la incorrecta definición de los métodos (confundidos con relaciones) y las deficiencias en la nomenclatura y atributos impiden alcanzar el nivel de corrección requerido para una puntuación superior.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Corregir el campo "Operaciones":** Deben listarse métodos reales con su firma (nombre, parámetros y tipo de retorno si aplica), centrados en el comportamiento interno de la clase. Ejemplo: `registrarDonacion(monto: Float): Boolean`, `calcularProgreso(): Integer`.
- **Revisar la nomenclatura:** Cambiar nombres verbales como `Hacer ruta` por sustantivos conceptuales (`Ruta`, `Trayecto` o `RegistroDeActividad`).
- **Completar atributos:** Alinear los atributos de cada clase con los datos especificados en los Requisitos de Información (IRQ). Por ejemplo, añadir `contraseña`, `edad` y `nombreUsuario` a la clase `Usuario`, y atributos como `especie`, `estado` y `ubicación` a la clase `Árbol`.
- **Separar responsabilidades:** Las multiplicidades y relaciones entre clases (ej. "0 o varias", "1 a muchos") deben documentarse en el diagrama de clases o en una matriz de relaciones, no en el campo de operaciones del glosario.