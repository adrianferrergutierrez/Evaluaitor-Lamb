# Evaluación: Descripción de actores

## Análisis
El documento incluye un apartado específico para la descripción de actores (Sección 8) y sus respectivas tablas de detalle (Tablas 22 a 27), donde se identifican seis actores: `ACT-001 Usuario`, `ACT-002 Personal de árboles`, `ACT-003 Administrador técnico`, `ACT-004 Administrador de gestión`, `ACT-005 GPS` y `ACT-006 Cuenta bancaria`. Sin embargo, la evaluación revela varias deficiencias que impiden alcanzar la máxima puntuación:

1. **Errores de identificación y copia/pega:** Las Tablas 26 y 27 repiten incorrectamente el identificador y nombre `ACT-004 ADMINISTRADOR DE GESTIÓN` en sus encabezados, cuando por el contenido y la lista de la Sección 8 deberían corresponder a `ACT-005 GPS` y `ACT-006 CUENTA BANCARIA`. Este error de consistencia afecta directamente la trazabilidad y la claridad del documento.
2. **Descripciones superficiales:** Las descripciones de los actores se limitan a una única frase (ej. *"Este actor representa a los usuarios que se descarga la app"*). No se detallan roles, responsabilidades, flujos de interacción principales ni se especifica si son actores primarios, de apoyo o pasivos, a pesar de que el propio glosario (Sección 17) define esta clasificación y menciona el uso del Método de Durán y Bernárdez.
3. **Clasificación de actores secundarios:** `GPS` y `Cuenta bancaria` son sistemas externos o dispositivos. Su inclusión como actores es aceptable en UML si se clasifican como **actores de apoyo**, pero el documento no justifica esta decisión ni los diferencia claramente de los actores humanos, lo que resta rigor metodológico.
4. **Diagrama asociado:** El documento cuenta con un "Diagrama de casos de uso" (Sección 7), que es donde normalmente se representan los actores. Aunque el diagrama existe, las inconsistencias en las tablas de descripción y la falta de profundidad en la caracterización de los roles hacen que la representación global no sea óptima.

En conjunto, los actores **sí están descritos**, por lo que se descarta la puntuación de 0/10. La presencia del diagrama y las tablas evita el 4/10. No obstante, los errores de identificación, la brevedad de las descripciones y la falta de clasificación metodológica sitúan la evaluación en el nivel intermedio.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Corregir errores de formato:** Revisar y corregir los encabezados de las Tablas 26 y 27 para que reflejen correctamente `ACT-005 GPS` y `ACT-006 CUENTA BANCARIA`.
- **Profundizar en las descripciones:** Ampliar cada tabla de actor incluyendo: tipo de actor (principal, de apoyo o pasivo), objetivos que persigue al interactuar con el sistema, y una descripción más detallada de sus responsabilidades y límites de interacción.
- **Justificar actores no humanos:** Explicar explícitamente por qué `GPS` y `Cuenta bancaria` se modelan como actores (sistemas externos de apoyo) y cómo se comunican con el sistema (protocolos, APIs, etc.).
- **Alinear con la metodología:** Aplicar la plantilla del Método de Durán y Bernárdez mencionada en el glosario para estandarizar la descripción de actores y garantizar coherencia con el resto de la documentación.
- **Verificar coherencia con el diagrama:** Asegurar que todos los actores listados en las tablas aparezcan correctamente nombrados y conectados en el Diagrama de Casos de Uso (Sección 7), y que no existan actores en el diagrama que no estén documentados en las tablas.