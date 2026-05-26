# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El diagrama de clases del modelo de dominio (presentado en la Imagen 31 y detallado en el Glosario de clases, Tablas 43-53) muestra un esfuerzo estructurado y una aplicación correcta de la notación UML estándar. Se identifican claramente las clases principales del dominio (`Usuario`, `Donación`, `Objetivo`, `Ruta Predeterminada`, `Ruta no predeterminada`, `Empresa de plantación`, `Árbol`, `Zona`, `Mantenimiento` y `Tipo Transporte`), se especifican atributos con sus tipos de dato, se utilizan estereotipos adecuados (`<<enumeration>>`) y se definen asociaciones con multiplicidades y nombres de rol.

Sin embargo, al contrastarlo con los principios de un **modelo de dominio conceptual** y con la especificación de requisitos del documento, se detectan varias desviaciones:
1. **Mezcla de conceptos de dominio con detalles de implementación:** Un modelo de dominio debe representar entidades del mundo real, no componentes software. Atributos como `Contraseña` en `Empresa de plantación`, o `Iniciar: Boolean` / `Parar: Boolean` en `Ruta no predeterminada`, corresponden a lógica de interfaz o seguridad, no al dominio del negocio.
2. **Clase `Hacer ruta`:** Esta clase representa una acción/caso de uso, no un concepto del dominio. En un modelo conceptual debería modelarse como `RegistroDeRuta`, `Trayecto` o `Actividad`, y las rutas predeterminadas/no predeterminadas deberían ser especializaciones o estados de esa entidad.
3. **Multiplicidades inconsistentes:** La relación `Donación → Empresa de plantación` indica `0..1` a `1`, lo que implicaría que una empresa solo puede recibir una donación en toda su existencia. Lo correcto sería `0..*` en el extremo de la empresa. Asimismo, la clase `Árbol` incluye un atributo `Cantidad: Integer`, lo cual es conceptualmente incorrecto para una entidad que representa un árbol individual; la cantidad debería ser un atributo de la relación o de una clase agregadora.
4. **Omisión de requisitos clave:** El objetivo `OBJ-003 Competencia amistosa` y el requisito `IRQ-001` mencionan explícitamente la gestión de amistades y la competencia. No existe ninguna clase `Amistad`, `Seguidor` o `RedSocial` que refleje esta relación muchos-a-muchos entre usuarios, dejando un vacío importante respecto a la especificación.

En conjunto, la notación UML está bien aplicada y la estructura base es coherente, pero el diagrama no es completamente correcto desde una perspectiva conceptual y omite o modela incorrectamente algunas relaciones y clases derivadas de los requisitos. Esto se ajusta al nivel de 7/10 de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Purificar el modelo conceptual:** Eliminar atributos de implementación (`Contraseña`, `Iniciar`, `Parar`, `Mantenimiento a realizar`) y trasladarlos al diseño técnico o al modelo de datos físico.
- **Replantear `Hacer ruta`:** Sustituir esta clase por una entidad de dominio como `RegistroDeRuta` o `Actividad`, y utilizar herencia o un atributo discriminador para diferenciar rutas predeterminadas de espontáneas.
- **Corregir multiplicidades:** Revisar todas las cardinalidades, especialmente `Donación ↔ Empresa de plantación` (debe ser `0..*` en la empresa) y `Árbol` (eliminar `Cantidad` como atributo de la entidad individual).
- **Incluir la dimensión social:** Añadir una clase `Amistad` o `VinculoSocial` con atributos como `fechaCreacion` o `estado`, y relacionarla con `Usuario` (asociación reflexiva muchos-a-muchos) para cubrir el requisito de competencia amistosa.
- **Validar contra la matriz de requisitos:** Cruzar sistemáticamente cada IRQ y OBJ con las clases y relaciones del diagrama para asegurar que no queden funcionalidades críticas sin representación conceptual.