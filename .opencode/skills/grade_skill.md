# grade_skill

## Role

Calcula la nota ponderada de forma determinística. Úsala cuando tengas puntuaciones parciales (0–10) por criterio.

## Tools

| # | Herramienta | Módulo | Qué hace |
|---|-------------|--------|----------|
| 1 | `grade` | `core/grading/grader.py` | Calcula nota ponderada y media aritmética (determinístico, sin LLM) |

## Cuándo usar

- Ya tienes `scores.json` de `evaluate_criteria` y quieres recalcular con otros pesos
- Tienes puntuaciones de evaluación manual
- Necesitas la nota final ponderada según pesos de rúbrica
- Nunca calcules la nota manualmente

## Uso

### Desde puntuaciones directas

```bash
python core/grading/grader.py --scores 7 8.5 9
```

### Desde archivos de evaluación

```bash
python core/grading/grader.py \
  --eval-md eval_obj.md:objetivos eval_cu.md:casos_uso \
  --config configs/rubric_architecture.yaml
```

### Desde JSON de criterios

```bash
python core/grading/grader.py --criteria-json criteria.json
```

### Desde Python

```python
from core.grading.grader import RubricGrader

grader = RubricGrader.from_config("configs/rubric_architecture.yaml")
result = grader.grade(eval_results)  # {criterion_id: markdown_text}
print(result.weighted_final, result.mean_xbar)
```

## Reglas

- Verifica que las puntuaciones están en rango 0–10
- Verifica que los pesos suman ~1.0
- Nunca recalcules la nota — usa siempre el output de esta herramienta

## Output

JSON con `weighted_final`, `mean_xbar`, y `performance_level`.
