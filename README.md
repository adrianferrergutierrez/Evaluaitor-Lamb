# SE-Agentic-Evaluator

Asistente agéntico para evaluación asistida por IA generativa, diseñado para **complementar** el juicio docente, **no sustituirlo**.

## Propósito
Este repositorio transforma un pipeline rígido de investigación (Extracción → Coherencia → Evaluación por Criterios → Síntesis) en una **Skill agéntica** para la plataforma **opencode.ai**, permitiendo:
- Selección dinámica de herramientas según el contenido (texto, tablas, PDFs, diagramas).
- Priorización de privacidad: uso de **modelos locales** para cumplimiento **RGPD** cuando sea posible.
- Trazabilidad: cada afirmación evaluativa debe poder vincularse a evidencia del documento.

## Fases conceptuales (no estrictamente secuenciales)
Aunque el sistema original se describía en cuatro fases, el agente de este repo **no está obligado a seguir un orden fijo**:
1. Extracción (texto/figuras/diagramas)
2. Análisis de coherencia, completitud y trazabilidad
3. Evaluación por criterios (SMART, ISO/IEC 25010, rúbrica)
4. Síntesis y retroalimentación

## Estructura del repositorio
- `.opencode/skills/evaluator_skill.md`: definición de la Skill (system prompt) para opencode.ai.
- `core/extraction/`: extracción de información desde PDFs e imágenes/diagramas (conceptos tipo DiagramLens).
- `core/analysis/`: trazabilidad, completitud, detección de “requisitos huérfanos”.
- `core/grading/`: cálculo determinista de la calificación final mediante script Python (evita alucinaciones).
- `prompts/`: prompts de trabajo (prompt1_1 ... prompt4_1) en Markdown.
- `docs/`: documentación técnica y referencia a la rúbrica original.

## Nota ética y de uso
Este sistema debe emplearse como herramienta de apoyo. La calificación final y decisiones académicas deben permanecer bajo responsabilidad del profesorado.
