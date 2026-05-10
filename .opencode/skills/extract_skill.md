# extract_skill

## Role

Extrae elementos semánticos del entregable: objetivos, requisitos, casos de uso y descripciones de diagramas. Úsala cuando necesites identificar y formalizar los elementos del documento de forma independiente.

**Nota**: Si usas `evaluate_criteria` con `--full`, estas herramientas se ejecutan automáticamente como parte del pipeline.

## Tools

| # | Herramienta | Módulo | Qué hace |
|---|-------------|--------|----------|
| 1 | `extract_objectives` | `core/extraction/objectives.py` | Extrae objetivos (OBJ-X) con prompt `1_1_extraccion_objetivos.md` |
| 2 | `extract_requirements` | `core/extraction/requirements.py` | Extrae IRQ y NFR con prompt `1_2_extraccion_requisitos.md` |
| 3 | `extract_use_cases` | `core/extraction/use_cases.py` | Extrae casos de uso (CU-XXX) con prompt `1_3_extraccion_casos_de_uso.md` |
| 4 | `describe_diagrams` | `core/extraction/diagramlens/` | Describe diagramas con modelo de visión local (`qwen3-vl`) |

## Cuándo usar cada herramienta

- **Solo necesitas objetivos** → `extract_objectives`
- **Solo necesitas requisitos** → `extract_requirements`
- **Necesidades casos de uso** → `extract_use_cases`
- **Imágenes de diagramas** → `describe_diagrams` (si `extract_use_cases` reporta diagramas)
- **Evaluación completa** → Usa `evaluate_criteria` con `--full` (ejecuta todo automáticamente)

## Reglas

- Fidelidad al original: no inventes ni parafrasees
- Preserva IDs originales (OBJ-X, IRQ-Y, CU-ZZZ, NFR-Z)
- Si hay diagramas, describe cada uno con `describe_diagrams` antes de evaluar

## Inputs

- Markdown del entregable (convertido desde PDF con `pdf_extract_skill` si aplica)
- Imágenes de diagramas referenciadas como `![alt](path)`

## Output

- Lista de objetivos (OBJ-X)
- Lista de requisitos funcionales (IRQ-Y) y no funcionales (NFR-Z)
- Lista de casos de uso (CU-XXX)
- Descripciones técnicas de diagramas
