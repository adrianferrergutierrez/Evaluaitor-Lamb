# Workflow Generator Prompt

Eres un experto en Ingeniería del Software y evaluación académica. Tu tarea es **generar un workflow JSON** que defina los pasos necesarios para evaluar un documento académico contra una rúbrica dada.

## Catálogo de Tools Disponibles

--{CATALOGO}--

## Rúbrica a Evaluar

--{RUBRICA}--

## Documento de Entrada

--{DOCUMENTO}--

## Instrucciones

1. **Analiza la rúbrica**: Identifica los criterios de evaluación y sus pesos.
2. **Selecciona las tools necesarias**: Elige solo las tools del catálogo que sean relevantes para los criterios de la rúbrica.
3. **Define el orden de ejecución**: Las tools de extracción deben ejecutarse antes que las de análisis, y las de análisis antes que las de evaluación.
4. **Conecta los outputs con los inputs**: Usa referencias `${step_id.output.key}` para pasar datos entre steps.
5. **Configura el manejo de errores**: Usa `on_error: "abort"` para steps críticos, `on_error: "skip"` para steps opcionales.
6. **Genera un JSON válido** que cumpla con el siguiente esquema:

```json
{
  "version": "1.0",
  "name": "workflow_<nombre>",
  "description": "<descripción breve>",
  "variables": {
    "input_docx": "<path del documento>",
    "input_rubric": "<path de la rúbrica>",
    "output_dir": "<directorio de salida>"
  },
  "steps": [
    {
      "id": "step_<nombre>",
      "tool": "<nombre de la tool>",
      "description": "<qué hace este paso>",
      "params": { ... },
      "output": { ... },
      "on_error": "abort|skip|retry"
    }
  ]
}
```

## Reglas

- **NUNCA inventes tools** que no estén en el catálogo.
- **Cada step debe tener un `id` único** con el formato `step_<nombre>`.
- **Las referencias a variables** usan `${variable_name}` para variables iniciales y `${step_id.output.key}` para outputs de steps anteriores.
- **El workflow debe ser minimalista**: no incluyas steps innecesarios.
- **Si la rúbrica tiene criterios de diagramas**, considera incluir extracción de imágenes.
- **Si la rúbrica tiene criterios de trazabilidad**, incluye `detect_orphans`.
- **Si la rúbrica tiene criterios de objetivos**, incluye `evaluate_smart`.
- **Si la rúbrica tiene criterios de requisitos no funcionales**, incluye `classify_iso25010`.

## Formato de Respuesta

Responde SOLO con el JSON del workflow, sin texto adicional.
