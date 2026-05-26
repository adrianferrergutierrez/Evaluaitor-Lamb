# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **13. Glosario de clases** (Tablas 43 a 53), donde se detallan 11 clases correspondientes al modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. Cada clase cuenta con una tabla estructurada que incluye su descripción, atributos y operaciones, cumpliendo así con los requisitos formales del criterio.

No obstante, al evaluar la corrección técnica y semántica de los contenidos, se identifican varias desviaciones respecto a las buenas prácticas de UML y modelado de dominio:
- **Confusión entre Operaciones y Asociaciones:** En la mayoría de las tablas, el campo `Operaciones` no describe métodos o comportamientos propios de la clase (ej. `registrar()`, `calcular()`, `actualizarEstado()`), sino que se utiliza para describir relaciones, multiplicidades o interacciones con otras clases. Por ejemplo, en *Usuario* se indica: `"Enviar donación: el usuario puede enviar 0 o varias donaciones a una empresa de plantación"`, y en *Árbol*: `"Zona: La empresa planta el árbol en una zona asignada..."`. Esto corresponde a asociaciones estructurales, no a operaciones de comportamiento.
- **Atributos con enfoque de interfaz de usuario:** Algunos atributos mezclan conceptos del modelo de dominio con elementos de UI, como `Iniciar (Boolean): “botón” de inicio`, `Parar (Boolean): “botón” de parar` o `Completado (Boolean): “botón” para marcar...`. En un modelo de dominio, los atributos deben representar datos o estados del negocio, no controles de pantalla.
- **Nomenclatura inadecuada:** La clase `Hacer ruta` está nombrada como un verbo/caso de uso. En un modelo de dominio, las clases deben ser sustantivos que representen entidades conceptuales (ej. `Ruta` o `RegistroDeRuta`).
- **Clase `Tipo de transporte`:** Correctamente estereotipada como `<<enumeration>>`, aunque se indica que carece de atributos y operaciones, lo cual es coherente con su naturaleza.

A pesar de estas imprecisiones conceptuales, el glosario cubre todas las clases del diagrama, explica su significado y proporciona listados de atributos y operaciones, por lo que se ajusta al nivel de **7/10** de la rúbrica, aunque con margen de mejora técnica para alcanzar la excelencia.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Corregir el campo "Operaciones":** Sustituir las descripciones de relaciones por firmas de métodos reales que definan el comportamiento de la clase (ej. `crearRuta()`, `registrarDonacion(monto)`, `actualizarEstado()`, `calcularProgreso()`).
- **Separar modelo de dominio de interfaz:** Eliminar referencias a "botones" o elementos de UI en los atributos. Los atributos deben reflejar exclusivamente datos del negocio (ej. `fechaInicio`, `estado`, `distanciaRecorrida`, `esMantenimientoRequerido`).
- **Revisar nomenclatura:** Cambiar `Hacer ruta` por un sustantivo propio de dominio como `Ruta` o `Actividad`.
- **Añadir visibilidad y tipos:** Para mayor rigor académico, incluir la visibilidad de los atributos/métodos (`+`, `-`, `#`) y especificar correctamente los tipos de retorno y parámetros en las operaciones.
- **Coherencia con el diagrama de clases:** Asegurar que las multiplicidades y roles descritos en el glosario coincidan exactamente con las líneas de asociación del diagrama de clases, evitando duplicar información estructural en el campo de operaciones.