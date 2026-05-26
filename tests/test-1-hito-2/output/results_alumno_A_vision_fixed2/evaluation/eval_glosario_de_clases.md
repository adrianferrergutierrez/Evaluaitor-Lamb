# Evaluación: Glosario de clases

## Análisis
El documento incluye el apartado **13. Glosario de clases**, desarrollado mediante las Tablas 43 a 53. En total, se documentan 11 clases conceptuales del modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`.

Cada entrada sigue una estructura uniforme que cubre los tres elementos exigidos por la rúbrica:
1. **Significado/Descripción:** Todas las clases cuentan con una descripción clara y contextualizada en el dominio del problema (ej. *"Representa a las personas que utilizan la aplicación"*, *"Lugares en los que están plantados los árboles..."*).
2. **Atributos:** Se listan los atributos principales junto con su tipo de dato (`String`, `Boolean`, `Float`, `Integer`), lo que demuestra un nivel de detalle adecuado para un modelo de dominio.
3. **Métodos/Operaciones:** Se incluyen en todas las tablas. Sin embargo, se observa que muchas están redactadas como **asociaciones o relaciones entre clases** (ej. `"Usuario: el usuario puede hacer una ruta 0 o muchas veces"`, `"Zona: la zona en la que se plantan los árboles puede estar vacía todavía..."`). En UML, esto corresponde a la definición de multiplicidades y roles en el diagrama, no a comportamientos o métodos propios de la clase. Aun así, la intención de documentar responsabilidades y comportamientos conceptuales está presente y cumple con el requisito de inclusión.

Dado que se han descrito todas las clases, se ha explicado su significado y se han incluido atributos y operaciones principales, el trabajo se ajusta al nivel de **7/10** establecido en la rúbrica. La cobertura es completa y la estructura es coherente, aunque la formulación de las operaciones presenta una confusión conceptual leve entre métodos y relaciones.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Diferenciar operaciones de asociaciones:** En un glosario de clases UML, las operaciones deben representar comportamientos o servicios que la clase ejecuta (ej. `registrarRuta()`, `calcularDistancia()`, `actualizarEstado()`, `procesarDonación()`). Las relaciones y multiplicidades deben reservarse para el diagrama de clases. Se recomienda revisar las tablas para reformular las "operaciones" como acciones reales.
- **Refinar atributos de referencia:** En clases como `Árbol` o `Mantenimiento`, atributos como `Usuario (String)` o `Empresa de plantación` deberían modelarse como referencias a objetos o identificadores (`idUsuario`, `idEmpresa`) para mantener la coherencia con el modelo de dominio.
- **Consistencia con el diagrama:** Verificar que cada clase del glosario tenga su contraparte exacta en el diagrama de clases (Sección 12) y que los tipos de datos y responsabilidades coincidan.
- **Nota sobre la rúbrica:** El nivel `10/10` indica `"10%"`, lo cual parece un error tipográfico. Asumiendo que se refiere a un nivel de excelencia, el trabajo actual se acerca, pero requiere el ajuste conceptual mencionado en las operaciones para alcanzar la máxima puntuación.
- **Recomendación general:** El glosario está bien estructurado, es completo y cumple con los criterios académicos básicos. Con una revisión de nomenclatura UML para las operaciones, podría elevarse fácilmente a un nivel superior.