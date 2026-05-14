# Evaluación: Objetivos

## Análisis
El documento define los objetivos de manera explícita y estructurada, cumpliendo con los estándares esperados en un proyecto de ingeniería del software. En la sección **1.2 Objetivos** se establece un objetivo principal alineado con el ODS 1 (Fin de la pobreza), centrado en facilitar el acceso a recursos sociales para personas en situación de vulnerabilidad mediante una plataforma segura, accesible y centralizada. Posteriormente, en las **Tablas 2 a 6**, se desglosan cinco objetivos funcionales concretos (OBJ-001 a OBJ-005) que cubren: gestión de usuarios, gestión de donaciones, disponibilidad de comedores y refugios, solicitud de becas/ayudas y gestión de voluntariado. Cada objetivo incluye metadatos relevantes (versión, autores, descripción, importancia, urgencia, estado y estabilidad), lo que refleja una buena práctica de gestión de requisitos.

Además, el documento incorpora **matrices de trazabilidad** (Sección 2.5) que vinculan explícitamente los objetivos con los requisitos de información, restricciones, requisitos no funcionales y casos de uso, garantizando cobertura y coherencia en el desarrollo. También se mencionan objetivos de aprendizaje y trabajo en equipo, adecuados para un contexto académico.

Sin embargo, los objetivos presentan algunas áreas de mejora: la descripción de OBJ-003 contiene una repetición textual innecesaria; los campos de "Subobjetivos" están vacíos en todas las tablas; y no se incluyen métricas cuantificables o indicadores de éxito que permitan evaluar el cumplimiento real de cada objetivo. Aunque están bien fundamentados y son funcionales, no aportan un enfoque innovador o diferenciador que destaque frente a soluciones existentes en el ámbito de la asistencia social digital, por lo que no alcanzan el nivel de originalidad requerido para la máxima puntuación.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Completar los subobjetivos:** Definir descomposiciones funcionales o hitos intermedios para cada objetivo principal facilitará la planificación y el seguimiento del desarrollo.
- **Añadir criterios de aceptación medibles:** Incorporar KPIs o umbrales cuantificables (ej. "tiempo de respuesta < 2s", "cobertura del 95% de comedores municipales", "tasa de conversión de solicitudes > X%") permitirá validar el cumplimiento de los objetivos de forma objetiva.
- **Revisar y depurar descripciones:** Eliminar repeticiones (como en OBJ-003) y asegurar que cada descripción sea concisa, técnica y alineada con el alcance del sistema.
- **Formalizar objetivos de accesibilidad:** Dado que en la introducción se menciona explícitamente la inclusión de personas con discapacidades visuales, auditivas o motoras, sería recomendable crear un objetivo específico o subobjetivo dedicado a la accesibilidad (WCAG 2.1, lectores de pantalla, navegación por teclado, etc.).
- **Mantener coherencia entre narrativa y tablas:** Asegurar que la sección 1.2 y las tablas de objetivos compartan la misma terminología y nivel de detalle para evitar ambigüedades durante la implementación.