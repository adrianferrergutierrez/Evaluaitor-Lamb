# Evaluación: Requisitos no funcionales

## Análisis
El documento define explícitamente **cuatro requisitos no funcionales (NFR)**, localizados en las Tablas 44 a 47, que cubren categorías fundamentales de calidad del software:

1. **NFR-001 (Protección de datos):** Establece restricciones de acceso a información sensible según el rol del usuario y menciona el cumplimiento de la ley de protección de datos. Aunque aborda correctamente la dimensión de seguridad/privacidad, la redacción es algo genérica (`"cierta información privada"`) y carece de especificaciones técnicas o normativas concretas (ej. RGPD, cifrado, RBAC).
2. **NFR-002 (Rendimiento):** Define métricas claras y cuantificables: capacidad para procesar `1000 solicitudes simultáneas` con un `tiempo de respuesta promedio ≤ 2 segundos`. Es un requisito bien estructurado, verificable mediante pruebas de carga y alineado con estándares de ingeniería de software.
3. **NFR-003 (Usabilidad/Accesibilidad):** Especifica una funcionalidad de asistencia por voz para usuarios con discapacidad visual. Es concreto y responde directamente a la necesidad de inclusión mencionada en la introducción. No obstante, podría ampliarse para cubrir otras discapacidades citadas (auditiva, motora) o referenciar estándares internacionales (WCAG 2.1).
4. **NFR-004 (Disponibilidad):** Establece un SLA medible: `16 horas diarias de operación continua, 7 días a la semana`, con un máximo de `1 hora semanal de inactividad` para mantenimiento. Es realista, cuantificable y fácilmente monitorizable.

Cada NFR incluye metadatos relevantes (versión, autores, objetivos y requisitos asociados, importancia, urgencia, estado y comentarios), lo que demuestra una estructuración adecuada. En conjunto, se han descrito correctamente **más de 3 requisitos no funcionales**, cumpliendo con los criterios de especificidad, medibilidad y relevancia para el sistema propuesto.

## Puntuación
**Puntuación:** 10/10

## Observaciones
- **Concretar NFR-001:** Reemplazar expresiones ambiguas por especificaciones técnicas y normativas explícitas (ej. `"Cumplimiento del RGPD/LOPDGDD"`, `"Cifrado AES-256 en tránsito y reposo"`, `"Control de acceso basado en roles (RBAC) con principio de mínimo privilegio"`).
- **Ampliar accesibilidad (NFR-003):** Dado que la introducción menciona discapacidades visuales, auditivas y motoras, se recomienda añadir criterios de cumplimiento de pautas WCAG 2.1 nivel AA, navegación por teclado, compatibilidad con lectores de pantalla estándar y subtítulos para contenido multimedia.
- **Incluir métodos de verificación:** Añadir a cada NFR una breve descripción de cómo se validará (ej. pruebas de estrés/JMeter para rendimiento, auditorías de seguridad/pentesting para protección de datos, monitorización con herramientas tipo UptimeRobot para disponibilidad).
- **Consistencia estructural:** La sección `2.4- Requisitos no funcionales` aparece vacía en el cuerpo principal del documento, mientras que las tablas están más adelante. Se recomienda unificar su ubicación o añadir referencias cruzadas para mejorar la trazabilidad y legibilidad del documento.