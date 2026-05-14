# Evaluación: Ética informática

## Análisis
El documento aborda la ética informática de manera explícita y estructurada, cumpliendo con los criterios del nivel 7/10. Se identifica una sección dedicada (**2.6 Ética de la informática**) donde se declara el compromiso con la privacidad, el cumplimiento de la ley de protección de datos y el propósito social del sistema (reducir la desigualdad y facilitar el acceso a recursos esenciales para personas vulnerables, alineado con el ODS 1). 

Los principios éticos se materializan en la documentación a través de requisitos concretos:
- **Privacidad y protección de datos:** NFR-001 establece restricciones de acceso y cumplimiento normativo. CRQ-004 y CRQ-005 refuerzan la seguridad mediante contraseñas robustas y autenticación obligatoria.
- **Accesibilidad e inclusión:** NFR-003 contempla funcionalidades de lectura de pantalla para usuarios con discapacidad visual, y la introducción (1.1) menciona explícitamente la adaptación a diversas discapacidades.
- **Integridad y equidad en el uso de recursos:** CRQ-006 impide que un usuario acumule roles de voluntario y beneficiario simultáneamente, evitando conflictos de interés y asegurando que las ayudas lleguen a quienes realmente las necesitan.
- **Transparencia:** Se menciona un historial de donaciones y voluntariado para garantizar trazabilidad (1.2, IRQ-002, IRQ-006).

No obstante, la reflexión ética es concisa y se limita principalmente a la protección de datos y la finalidad social. No se abordan en profundidad otros aspectos clave de la ética informática contemporánea, como la posible sesgo algorítmico en la asignación de becas/ayudas, el uso ético de la IA mencionada en la sección 1.3, políticas de minimización y retención de datos, derecho al olvido, o la referencia a códigos deontológicos profesionales (ACM/IEEE). La sección 2.6 ocupa apenas un párrafo, lo que limita la profundidad del análisis.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Ampliar la sección 2.6:** Incluir un análisis de riesgos éticos específicos (ej. sesgos en la evaluación de vulnerabilidad, transparencia en la asignación automática de recursos, mecanismos de auditoría y rendición de cuentas).
- **Referenciar marcos éticos profesionales:** Citar explícitamente principios del código de ética ACM/IEEE o la normativa GDPR/RGPD para dar mayor solidez técnica y deontológica.
- **Profundizar en el uso de IA:** Dado que se menciona el uso de ChatGPT/Gemini como apoyo (1.3), añadir una declaración sobre su uso ético (ej. no delegar decisiones críticas en IA, verificación humana, transparencia con el usuario).
- **Requisitos de consentimiento y gobernanza de datos:** Incorporar CRQ/NFR adicionales que especifren el consentimiento explícito para el tratamiento de datos sensibles, políticas de retención/eliminación, y mecanismos de rectificación o portabilidad de datos.
- **Documentar pruebas de accesibilidad:** Incluir en los requisitos no funcionales métricas o estándares de accesibilidad (ej. WCAG 2.1) para validar la inclusión real de usuarios con discapacidad.