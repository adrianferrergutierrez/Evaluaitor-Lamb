# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **13. Glosario de clases** (Tablas 43 a 53), donde se detallan 11 clases del modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. Cada tabla sigue una estructura uniforme que incluye `Descripción`, `Atributos` y `Operaciones`, cumpliendo así con el requisito formal de listar todas las clases y explicar su significado.

Sin embargo, al evaluar la calidad técnica según la rúbrica, se detectan deficiencias conceptuales importantes en la descripción de los **métodos/operaciones**. En lugar de especificar comportamientos o funciones propias de cada clase (p. ej., `registrarRuta()`, `calcularDistancia()`, `actualizarEstado()`), el campo "Operaciones" se utiliza sistemáticamente para describir **relaciones, multiplicidades y flujos de casos de uso**. Evidencias claras:
- En *Hacer ruta* (Tabla 44): `"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."`
- En *Ruta predeterminada* (Tabla 45): `"Creada por un usuario: una ruta predeterminada puede ser creada por uno o varios usuarios..."`
- En *Empresa de plantación* (Tabla 52): `"Árbol: planta uno o varios árboles / Mantenimiento: se encarga del mantenimiento..."`
- En *Zona* (Tabla 53): `"Árbol: la zona en la que se plantan los árboles puede estar vacía todavía, o tener ya muchos registrados en ella"`

Esto indica una confusión entre operaciones de clase y asociaciones/multiplicidades del diagrama UML. Además, la clase `Hacer ruta` representa una acción o caso de uso, no una entidad conceptual del dominio, lo cual debilita la coherencia del modelo. Los atributos, aunque presentes, en algunos casos son redundantes o poco precisos (p. ej., `Árbol` incluye `Usuario (String)` y `Cantidad (Integer)` como atributos directos, cuando deberían modelarse mediante relaciones de asociación).

En conjunto, el glosario cumple con la estructura básica y describe todas las clases con su significado y atributos, pero **no explica correctamente los métodos principales**, situándose por debajo del nivel de 7/10 definido en la rúbrica.

## Puntuación
**Puntuación:** 5/10

## Observaciones
- **Corregir el campo "Operaciones":** Reemplazar las descripciones de relaciones y multiplicidades por métodos reales con firma clara (nombre, parámetros, tipo de retorno). Ejemplo: en `Usuario`, cambiar `"Enviar donación: el usuario puede enviar 0 o varias donaciones..."` por `registrarDonacion(monto: Float, metodoPago: String): Boolean`.
- **Revisar la naturaleza de las clases:** Eliminar o refactorizar `Hacer ruta`, ya que corresponde a un caso de uso o servicio de aplicación, no a una clase de dominio. Considerar una clase base `Ruta` con un atributo `tipo` o usar herencia si es estrictamente necesario.
- **Precisar atributos:** Asegurar que los atributos representen propiedades intrínsecas de la clase. Por ejemplo, `Árbol` no debería almacenar `Usuario` como `String`, sino mantener una asociación con la clase `Usuario`. Lo mismo aplica para `Mantenimiento` y `Zona`.
- **Completar enumeraciones:** En `Tipo de transporte`, listar explícitamente los valores permitidos (`ANDANDO`, `BUS`, `METRO`, `BICICLETA`, `PATINETE`) en el glosario para mayor claridad y trazabilidad con el código.
- **Alinear con el diagrama de clases:** Verificar que las operaciones y atributos del glosario coincidan exactamente con los mostrados en el diagrama de clases del modelo de dominio (Sección 12), manteniendo consistencia terminológica, tipos de datos y visibilidad.