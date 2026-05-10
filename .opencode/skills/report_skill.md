# report_skill

## Role

Genera el informe final de evaluación sintetizando evaluaciones previas. Úsala cuando tengas archivos `eval_*.md` y necesites un informe consolidado.

## Tools

| # | Herramienta | Módulo | Qué hace |
|---|-------------|--------|----------|
| 1 | `generate_report` | `core/evaluation/evaluator.py` | Genera `evaluacion_final.md` desde `eval_*.md` + `scores.json` |

## Cuándo usar

- Ya tienes evaluaciones individuales por criterio (`eval_*.md`) generadas por `analyze_skill`
- Ya tienes puntuaciones (`scores.json`)
- Necesitas un informe final consolidado

## Uso

### Con scores.json precomputado

```bash
python core/evaluation/evaluator.py \
  --document documento.md \
  --eval-dir output/evaluacion/ \
  --scores output/evaluacion/scores.json \
  --output output/evaluacion/
```

### Sin scores.json (el grader calcula las notas)

```bash
python core/evaluation/evaluator.py \
  --document documento.md \
  --eval-dir output/evaluacion/ \
  --config configs/rubric_architecture.yaml \
  --output output/evaluacion/
```

## Reglas

- El informe debe incluir: tabla de rúbrica, resumen ejecutivo, análisis por criterio con evidencias, huérfanos, SMART/ISO 25010, recomendaciones priorizadas
- Pie de página obligatorio: *"Este informe es una herramienta de apoyo. La calificación final es responsabilidad exclusiva del profesorado."*
- Todo juicio debe ir con evidencia (cita, diagrama, o ID)

## Inputs

- Documento Markdown original
- Directorio con `eval_*.md` (generados por `analyze_skill`)
- `scores.json` (opcional, si no existe se calcula desde `--config`)

## Output

- `evaluacion_final.md` — informe consolidado
