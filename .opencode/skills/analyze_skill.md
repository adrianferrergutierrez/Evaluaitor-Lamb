# analyze_skill

## Role

Analiza elementos extraídos y evalúa criterios de rúbrica contra el documento. Funciona en **modo agèntic**: tú decides qué herramientas usar y en qué orden basándote en lo que encuentres en el documento.

## Tools disponibles

| # | Herramienta | Módulo | Qué hace |
|---|-------------|--------|----------|
| 1 | `extract_objectives` | `core/extraction/objectives.py` | Extrae objetivos (OBJ-X) |
| 2 | `extract_requirements` | `core/extraction/requirements.py` | Extrae IRQ y NFR |
| 3 | `detect_orphans` | `core/analysis/orphans.py` | Detecta huérfanos (determinístico) |
| 4 | `check_smart` | `core/analysis/smart.py` | Evalúa objetivos SMART (determinístico) |
| 5 | `classify_iso25010` | `core/analysis/iso25010.py` | Clasifica NFR por ISO 25010 (determinístico) |
| 6 | `evaluate_criteria` | `core/evaluation/criterion_evaluator.py` | Evalúa criterios de rúbrica con contexto opcional |

## Flujo agèntic recomendado

Tú decides el orden, pero este es el patrón típico:

### Paso 1: Extraer elementos
```python
from core.extraction.objectives import extract_objectives
from core.extraction.requirements import extract_requirements

objectives_md = extract_objectives(document)
requirements_md = extract_requirements(document)
```

### Paso 2: Analizar (si hay elementos)
```python
from core.analysis.orphans import detect_orphans
from core.analysis.smart import evaluate_objectives_smart, smart_summary_markdown
from core.analysis.iso25010 import classify_requirements_iso25010

# Huérfanos (si hay objetivos Y requisitos)
orphans = detect_orphans(objectives_md, requirements_md)

# SMART (si hay objetivos)
smart_scores = evaluate_objectives_smart(objectives_md)
smart_md = smart_summary_markdown(smart_scores)

# ISO 25010 (si hay NFR)
iso_report = classify_requirements_iso25010(requirements_md)
iso_md = iso_report.as_markdown()
```

### Paso 3: Construir contexto
Crea un archivo Markdown con los resultados:
```markdown
### Objetivos Extraídos
{objectives_md}

### Requisitos Extraídos
{requirements_md}

### Detección de Huérfanos
{orphans.as_markdown()}

### Evaluación SMART
{smart_md}

### Clasificación ISO/IEC 25010
{iso_md}
```

### Paso 4: Evaluar criterios con contexto
```bash
python core/evaluation/criterion_evaluator.py \
  --document documento.md \
  --config configs/rubric_architecture.yaml \
  --output output/evaluacion/ \
  --context output/analysis_context.md
```

El LLM recibirá todo el contexto estructurado junto con el documento, lo que le permite evaluar con evidencia concreta en lugar de texto crudo.

## Reglas

- **Siempre** extrae objetivos y requisitos antes de evaluar (si el documento los tiene)
- **Siempre** ejecuta `detect_orphans` antes de emitir puntuaciones
- **Siempre** ejecuta `check_smart` si hay objetivos
- **Siempre** ejecuta `classify_iso25010` si hay NFR
- Si un criterio de rúbrica tiene `requires_vision: true`, el modelo de visión analiza las imágenes del documento

## Inputs

- Documento Markdown completo
- YAML de rúbrica

## Output

- `eval_<criterio>.md` — evaluación por criterio con contexto inyectado
- `scores.json` — puntuaciones extraídas
- Archivos intermedios de extracción y análisis (si los generaste)
