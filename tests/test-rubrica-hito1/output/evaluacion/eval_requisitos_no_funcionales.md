# Evaluación: Requisitos no funcionales

## Análisis
El documento cuenta con una sección específica (Apartado 6) dedicada a los requisitos no funcionales, donde se listan y detallan un total de **9 requisitos** (NFR-001 a NFR-009). Cada uno dispone de su tabla de especificación correspondiente (Tablas 13 a 21) que incluye identificación, versión, autores, objetivos asociados, requisitos asociados y una descripción funcional.

Los requisitos cubren categorías clásicas de ingeniería de software:
- **Seguridad:** NFR-001 (encriptación y autenticación segura).
- **Usabilidad:** NFR-002 (interfaz intuitiva).
- **Portabilidad:** NFR-005 (disponibilidad en Android e iOS).
- **Rendimiento:** NFR-006 (tiempo de respuesta < 2 segundos).
- **Mantenibilidad:** NFR-007 (documentación del código) y NFR-008 (buenas prácticas, arquitectura modular, pruebas).
- **Disponibilidad/Confiabilidad:** NFR-009 (servidores redundantes).

Además, se incluyen NFR-003 y NFR-004, que técnicamente se acercan más a **restricciones de negocio o acuerdos de nivel de servicio (SLA)** con entidades externas, pero que en el contexto académico se aceptan como requisitos no funcionales de tipo normativo/proceso.

Según la rúbrica proporcionada, al haberse definido y descrito correctamente **más de 3 requisitos no funcionales**, el trabajo alcanza el nivel máximo de evaluación. Cabe señalar que, aunque las descripciones base son adecuadas, varios campos de las tablas (Importancia, Urgencia, Estado, Estabilidad, Comentarios) conservan el texto de plantilla sin completar (`<importancia del requisito>`, etc.), lo que indica que la especificación está en fase de borrador pero no invalida la definición estructural de los requisitos.

## Puntuación
**Puntuación:** 10/10

## Observaciones
- **Completar atributos de las tablas:** Rellenar los campos pendientes (Importancia, Urgencia, Estado, Estabilidad, Comentarios) para garantizar la trazabilidad y facilitar la priorización en futuras iteraciones.
- **Añadir criterios de verificación medibles:** Algunos requisitos son cualitativos o ambiguos (ej. NFR-002 "gráficos con suficiente calidad", NFR-004 "cumpliendo todas las leyes que deba"). Se recomienda especificar estándares o métricas concretas (ej. "cumplir heurísticas de Nielsen o WCAG 2.1", "encriptación AES-256 en tránsito y reposo", "tiempo de respuesta <2s en el 95% de las peticiones bajo carga de X usuarios concurrentes").
- **Clasificar correctamente restricciones externas:** Los NFR-003 y NFR-004 dependen de procesos físicos y marcos legales externos al software. Sería más preciso etiquetarlos como "Restricciones de negocio" o reformularlos para indicar cómo el sistema los soportará (ej. "El sistema deberá registrar, notificar y auditar el estado de la plantación en un plazo máximo de 30 días naturales").
- **Revisar consistencia en matrices:** Verificar que las asociaciones entre NFRs, objetivos y casos de uso estén correctamente reflejadas en las matrices de rastreabilidad (Apartados 10 y 11) para mantener la coherencia del modelo.