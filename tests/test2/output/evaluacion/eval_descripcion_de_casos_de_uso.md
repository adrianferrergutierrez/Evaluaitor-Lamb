# Evaluación: Descripción de casos de uso

## Análisis
El documento incluye un catálogo estructurado de casos de uso (CU-001 a CU-020) presentados en formato tabular. Cada caso de uso contiene sistemáticamente los elementos requeridos por la rúbrica: **descripción**, **precondiciones**, **secuencia normal** (pasos numerados), **poscondiciones** y **excepciones**. La mayoría de los casos (ej. CU-001, CU-002, CU-008, CU-017) presentan flujos claros, bien secuenciados y con alternativas definidas, lo que demuestra un nivel de detalle adecuado para la fase de requisitos.

En cuanto a la correspondencia con el diagrama, el documento hace referencia explícita a un diagrama de casos de uso (sección 2.3.3) y a una vista de interacción (sección 3.3) donde se listan los mismos identificadores de casos de uso. La numeración, los actores asociados y las relaciones implícitas son coherentes con la notación UML estándar, lo que sugiere una alineación correcta entre la documentación textual y los modelos gráficos.

No obstante, se detectan inconsistencias menores que impiden una puntuación perfecta:
- El **CU-010** se menciona en el texto como una operación CRUD que debería dividirse en cuatro tablas, pero no se incluye su tabla correspondiente en el catálogo.
- Existen **errores de copia-pega** en las descripciones: CU-018 y CU-019 comparten texto idéntico, y la descripción de CU-020 ("Gestionar becas y ayudas") habla erróneamente de "gestión de usuarios registrados".
- Algunos pasos de secuencias normales o excepciones aparecen vacíos o con redacción genérica (ej. CU-018 paso 4, CU-019 paso 4).
- Las tablas presentan celdas duplicadas o vacías en campos como "Rendimiento" y "Frecuencia", lo que resta uniformidad al documento.

A pesar de estos detalles, el documento cumple ampliamente con los requisitos del nivel más alto de la rúbrica, ya que define precondiciones, postcondiciones y excepciones para la totalidad de los casos documentados, y los flujos principales están correctamente desglosados.

## Puntuación
**Puntuación:** 9/10

## Observaciones
1. **Corregir descripciones duplicadas o incorrectas:** Revisar y reescribir las descripciones de CU-018, CU-019 y CU-020 para que reflejen fielmente la funcionalidad que cada caso de uso pretende modelar.
2. **Completar o justificar el CU-010:** Incluir la tabla correspondiente o documentar explícitamente cómo se ha desglosado en operaciones CRUD individuales (Crear, Leer, Actualizar, Eliminar) para mantener la trazabilidad completa.
3. **Rellenar campos vacíos:** Completar los pasos faltantes en secuencias normales y excepciones, y eliminar o unificar las celdas duplicadas en las tablas para mejorar la legibilidad y el rigor técnico.
4. **Validar correspondencia con el diagrama:** Asegurar que el diagrama de casos de uso (sección 2.3.3) incluya visualmente todos los casos de uso documentados, sus actores y las relaciones `<<include>>`, `<<extend>>` o generalización, verificando que la numeración y los flujos coincidan exactamente con las tablas.
5. **Estandarizar formato:** Unificar la estructura de todas las tablas de casos de uso para que campos como "Rendimiento" y "Frecuencia" tengan valores coherentes o se eliminen si no son relevantes para el alcance actual del proyecto.