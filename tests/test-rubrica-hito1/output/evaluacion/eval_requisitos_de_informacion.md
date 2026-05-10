# Evaluación: Requisitos de información

## Análisis
El documento define 8 requisitos de información (IRQ-001 a IRQ-008) y presenta sus respectivas tablas de especificación (Tablas 5 a 12). Sin embargo, al evaluar su calidad y completitud frente a la rúbrica, se identifican las siguientes evidencias:

1. **Campos incompletos con texto marcador:** En todas las tablas de IRQ, múltiples atributos de la plantilla contienen texto sin rellenar o marcadores de posición como `<tiempo medio de vida>`, `<nº medio de ocurr. simult.>`, `<importancia del requisito>`, `<urgencia del requisito>`, `<estado del requisito>` y `<estabilidad del requisito>`. Esto indica que los requisitos no han sido descritos correctamente ni completados según la metodología solicitada.
2. **Desalineación con los Casos de Uso (CU):** El campo `Datos` de varios IRQ omite información explícitamente mencionada en las tablas de casos de uso:
   - **IRQ-002/IRQ-003 (Rutas):** No incluyen `distancia recorrida`, `tiempo empleado` ni `recompensas`, datos que aparecen en la secuencia normal y comentarios del CU-002.
   - **IRQ-004/IRQ-005 (Objetivos/Historial):** Solo listan `Nombre`, `Descripción` y `Estado`. Faltan los valores métricos o umbrales mencionados en CU-003 y CU-004 (ej. `número de árboles`, `kilómetros`, `tiempo de ruta objetivo`).
   - **IRQ-008 (Empresa):** El campo `Datos` menciona vagamente `Información de registro del árbol`, pero no detalla atributos clave presentes en CU-008, CU-009 y CU-010 como `evidencia/foto`, `zona de plantación`, `estado de mantenimiento` o `fecha de registro`.
3. **Coherencia estructural:** Aunque la estructura base sigue el método de Durán y Bernárdez y los campos `Descripción` y `Objetivos asociados` están razonablemente redactados, la falta de concreción en los datos y los campos vacíos impiden considerar que estén "descritos correctamente".

Por tanto, el criterio se ajusta al nivel de **4/10**: los requisitos están definidos e identificados, pero no se han descrito correctamente debido a la presencia de marcadores sin completar y a la omisión de datos relevantes que sí aparecen en los casos de uso.

## Puntuación
**Puntuación:** 4/10

## Observaciones
- **Completar todos los campos de la plantilla:** Sustituir los marcadores `<...>` por valores reales estimados o justificados (ej. `Tiempo de vida: Permanente`, `Importancia: Alta`, `Estado: Definido`, etc.).
- **Alinear `Datos` con los Casos de Uso:** Revisar cada CU y extraer explícitamente todos los atributos de información que el sistema debe almacenar o procesar. Añadirlos al campo `Datos` del IRQ correspondiente (ej. añadir `distancia`, `tiempo`, `recompensa` a IRQ-002; `valor_objetivo`, `unidad_medida` a IRQ-004; `evidencia_fotográfica`, `coordenadas_zona`, `estado_mantenimiento` a IRQ-008).
- **Validar consistencia cruzada:** Asegurar que la matriz de objetivos-requisitos y la matriz de requisitos-requisitos reflejen fielmente las relaciones actualizadas tras completar los campos faltantes.
- **Eliminar duplicados o ambigüedades:** En IRQ-001 se repite `Contraseña` y `Nombre de usuario` en la lista de datos; unificar y estructurar mejor los atributos para evitar redundancias.