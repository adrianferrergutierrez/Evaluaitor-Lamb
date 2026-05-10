# Evaluación: Ética informática

## Análisis
El documento demuestra una consideración consciente de varios principios de la ética informática, reflejándolos de manera explícita en la documentación, aunque con un alcance limitado a ciertos pilares fundamentales.

- **Transparencia y honestidad académica/profesional:** En el apartado *2. Registro de uso de IA generativa*, el equipo declara de forma clara el uso de ChatGPT de manera “puntual y controlada” para reescritura y resolución de dudas. Esta práctica se alinea con los principios éticos de transparencia, autoría responsable y uso consciente de herramientas automatizadas.
- **Seguridad y confidencialidad de datos:** El requisito no funcional *NFR-001 Seguridad de los datos* establece que la información de autenticación debe estar “totalmente encriptada” y seguir “patrones de alta seguridad”. Esto aborda directamente la protección de la privacidad y la integridad de los datos personales, un eje central de la ética en el desarrollo de software.
- **Calidad, mantenibilidad y disponibilidad:** Los requisitos *NFR-008 Uso de buenas prácticas de desarrollo* y *NFR-009 Prevención de caídas* reflejan un compromiso ético con la ingeniería de software responsable, garantizando un código documentado, modular y un sistema fiable que no perjudique la experiencia del usuario por fallos evitables.
- **Responsabilidad social y medioambiental:** Aunque trasciende lo estrictamente técnico, el propósito de la aplicación (incentivar transporte sostenible, reforestación y actividad física) integra una dimensión ética de impacto positivo, lo cual refuerza el valor social del software desarrollado.

No obstante, la documentación no aborda de forma explícita otros aspectos críticos de la ética informática actual: no se menciona el cumplimiento normativo específico (RGPD/LOPDGDD), no se detallan mecanismos de consentimiento informado, minimización de datos, derecho de supresión, ni se consideran estándares de accesibilidad (WCAG) o implicaciones éticas de la gamificación/competencia entre usuarios. La reflexión ética está presente y documentada, pero no se integra de manera transversal ni exhaustiva en el ciclo de vida del software.

Por ello, el trabajo se ajusta al nivel de **7/10**: se tienen en cuenta principios éticos y se reflejan en la documentación a través de la solución planteada y de los requisitos no funcionales, aunque con margen claro de profundización y formalización.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- Incorporar un requisito explícito de cumplimiento normativo (RGPD/LOPDGDD) que detalle políticas de consentimiento, minimización de datos, cifrado en tránsito/reposo y procedimientos para el ejercicio de derechos ARCO.
- Añadir requisitos de accesibilidad (ej. WCAG 2.1 nivel AA) para garantizar que la aplicación sea inclusiva para usuarios con diversidad funcional.
- Ampliar el registro de uso de IA indicando cómo se valida la información generada, se evitan sesgos algorítmicos y se garantiza que no se introducen datos sensibles en herramientas externas.
- Crear una matriz o apartado breve que vincule explícitamente los principios éticos (privacidad, transparencia, sostenibilidad, inclusión) con los requisitos funcionales/no funcionales y casos de uso correspondientes, elevando la trazabilidad y el rigor ético del proyecto.