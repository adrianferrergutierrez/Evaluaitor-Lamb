# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento presenta un modelo de dominio que identifica las entidades principales del sistema (`Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación`, `Zona` y `Hacer ruta`). Sin embargo, al analizar el glosario de clases (Tablas 43-53) y la descripción del modelo, se detectan varios problemas conceptuales y de modelado que afectan su calidad:

1. **Falta de pureza conceptual**: Un modelo de dominio debe representar conceptos del mundo real, no elementos de interfaz o implementación. El glosario incluye atributos como `Completado (Boolean): “botón” para marcar...`, `Iniciar/Parar (Boolean): “botón”...`, `Contraseña` y `Número de cuenta`. Estos son detalles de UI o de capa de aplicación/seguridad, no conceptos de dominio.
2. **Nombrado incorrecto de clases**: `Hacer ruta` es un verbo/acción (propio de un caso de uso), no una entidad conceptual. Debería modelarse como `Ruta`, `RegistroDeActividad` o `Trayecto`.
3. **Relaciones mal modeladas**: En lugar de utilizar asociaciones UML con multiplicidades, se han representado relaciones como atributos de tipo `String` (ej. `Árbol` tiene `Usuario (String): identificador del usuario`). Esto rompe la semántica del modelo de dominio y dificulta la trazabilidad con los requisitos.
4. **Clases y relaciones faltantes según requisitos**: A pesar de que los requisitos (IRQ-001, IRQ-006, CU-005) y los objetivos destacan la funcionalidad de `Competencia amistosa` y `Compartir logros`, no existe una clase que modele la relación de `Amistad`, `Seguidor` o `RedSocial`. Tampoco se modela explícitamente `HistorialDeObjetivos` (IRQ-005) ni `Transacción/Pago` como entidad independiente de `Donaciones`.
5. **Notación y estructura**: Aunque se asume que el diagrama gráfico (imágenes adjuntas) utiliza notación UML, la documentación en el glosario refleja una comprensión mixta entre modelado conceptual y diseño técnico. Las operaciones listadas en las clases (ej. `Enviar donación`, `Crear ruta predeterminada`) son propias de la capa de aplicación o de los casos de uso, no del modelo de dominio, que debe centrarse en atributos y asociaciones.

En conjunto, el modelo está bien planteado en cuanto a la identificación de los actores y flujos principales, pero contiene **demasiados errores conceptuales** y omite relaciones clave derivadas de la especificación de requisitos, lo que lo aleja de un modelo de dominio robusto y listo para la fase de diseño.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Eliminar detalles de implementación/UI**: Retirar atributos como `"botón"`, `"opción"`, `"contraseña"` o `"número de cuenta"`. El modelo de dominio debe centrarse en el estado y las relaciones conceptuales de las entidades.
- **Corregir el nombrado de clases**: Cambiar `Hacer ruta` por un sustantivo conceptual como `Ruta` o `Actividad`. Las clases deben representar entidades, no acciones.
- **Modelar relaciones con asociaciones UML**: Sustituir los atributos `String` que representan relaciones por líneas de asociación con nombres claros y multiplicidades correctas (ej. `Usuario 1..* ─── 0..* Ruta`).
- **Incorporar conceptos faltantes**: Añadir clases o asociaciones para `Amistad`/`Seguidor` (requerido por CU-005 e IRQ-006) y `HistorialDeObjetivos` o `Logro` (IRQ-005). Considerar `Transacción` como entidad independiente si se requiere trazabilidad de pagos.
- **Revisar el propósito de las operaciones**: En un modelo de dominio conceptual, las operaciones suelen omitirse o limitarse a comportamientos intrínsecos del concepto. Las acciones de negocio deben quedar reflejadas en los casos de uso o en el diseño de la capa de aplicación.
- **Consultar guías de modelado conceptual**: Revisar la diferencia entre modelo de dominio (conceptual), modelo de diseño (técnico) y diagrama de casos de uso para evitar solapamientos que reduzcan la claridad y utilidad del artefacto.