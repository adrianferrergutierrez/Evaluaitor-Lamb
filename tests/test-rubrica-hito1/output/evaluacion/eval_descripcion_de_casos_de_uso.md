# Evaluación: Descripción de casos de uso

## Análisis
El documento presenta una sección dedicada exclusivamente a la descripción de casos de uso (Apartado 9, Tablas 28 a 42), donde se detallan 15 casos de uso (CU-001 a CU-015). Cada tabla sigue una estructura formal y completa que incluye:
- **Descripción** clara del objetivo del caso de uso.
- **Precondición** y **Poscondición** explícitas para cada escenario.
- **Secuencia normal** desglosada en pasos numerados (p1, p2, etc.) que diferencian claramente las acciones del actor y las respuestas del sistema.
- **Excepciones** referenciadas a los pasos correspondientes, con acciones correctivas o mensajes de error definidos.
- Atributos adicionales de calidad (Rendimiento, Frecuencia, Importancia, Urgencia, Estado, Estabilidad).

Esta estructura supera ampliamente el umbral del nivel 7/10, ya que **todos** los casos de uso incluyen precondiciones, postcondiciones y manejo de excepciones. Los flujos principales son lógicos, coherentes con la funcionalidad descrita en los objetivos y requisitos, y siguen una notación estándar (compatible con el método de Durán y Bernárdez citado en el glosario). 

En el Registro de Cambios (Sección 1) se indica que los casos de uso fueron revisados, corregidos y ampliados en hitos anteriores, y que se alinearon con el diagrama de casos de uso (Sección 7). Aunque no es posible verificar visualmente la correspondencia exacta con la imagen del diagrama, la numeración y los nombres en el índice (9.1 a 9.15) coinciden con las tablas desarrolladas, lo que sugiere una trazabilidad interna consistente.

Se detectan leves inconsistencias de numeración en las tablas (por ejemplo, CU-011 se repite para "Gestionar usuarios", "Activar usuarios" y "Desactivar usuarios"; CU-012 y CU-013 aparecen en el índice pero no como encabezados de tabla), pero estos son errores de formato que no afectan la calidad ni la completitud de las descripciones funcionales.

## Puntuación
**Puntuación:** 10/10

## Observaciones
- **Corregir la numeración de las tablas:** Asegurar que cada caso de uso tenga un identificador único y secuencial (CU-011, CU-012, CU-013, CU-014, CU-015) y que coincida exactamente con el índice y el diagrama de casos de uso.
- **Validar correspondencia visual con el diagrama:** Revisar que los nombres, actores y relaciones en el diagrama (Sección 7) coincidan literalmente con los encabezados y actores principales de cada tabla.
- **Estandarizar la redacción de pasos:** En algunos casos, los pasos de la secuencia normal mezclan acciones del actor y del sistema en una misma línea. Se recomienda separarlas explícitamente (ej. `pX: El actor realiza...` / `pY: El sistema responde...`) para mayor claridad en la implementación futura.
- **Documentar flujos alternativos:** Si bien las excepciones están bien definidas, considerar añadir una sección de "Flujos alternativos" para escenarios válidos que no sean errores (ej. usuario que cancela una donación a mitad de proceso), lo que enriquecería la especificación.