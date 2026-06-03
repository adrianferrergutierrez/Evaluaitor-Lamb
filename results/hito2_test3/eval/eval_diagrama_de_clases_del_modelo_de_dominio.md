# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye el diagrama de clases del modelo de dominio (apartado 12) y su glosario asociado (apartado 13, tablas 43 a 53). Sin embargo, al analizar su contenido se detectan deficiencias estructurales y conceptuales que impiden considerarlo un modelo de dominio válido según los estándares de UML e Ingeniería del Software:

1. **Enfoque no conceptual:** Se incluyen clases que representan acciones o flujos de casos de uso en lugar de entidades del negocio. El ejemplo más claro es la clase `Hacer ruta`, que describe una interacción del usuario, no un concepto del dominio. En un modelo de dominio solo deben aparecer entidades, valores y relaciones conceptuales.
2. **Atributos inadecuados para el dominio:** Varios atributos reflejan estados de interfaz o controles de UI en lugar de propiedades del negocio. Por ejemplo, `Iniciar (Boolean)` y `Parar (Boolean)` en `Ruta no predeterminada`, o `Mantenimiento a realizar(Boolean)` en `Mantenimiento`. Estos deberían modelarse como fechas, estados (ej. `Estado: Enum {Pendiente, EnCurso, Finalizado}`) o tipos de mantenimiento.
3. **Uso incorrecto de la columna “Operaciones”:** En el glosario, las “Operaciones” se utilizan para describir relaciones, multiplicidades y pasos de casos de uso (ej. *“Usuario: el usuario puede hacer una ruta 0 o muchas veces...”*). En un modelo de dominio, las relaciones deben representarse explícitamente mediante asociaciones con roles y cardinalidades en el diagrama, y las operaciones (si se incluyen) deben ser responsabilidades conceptuales de alto nivel, no flujos de interacción.
4. **Granularidad y cobertura incompleta:** La clase `Árbol` contiene un atributo `Cantidad (Integer)`, lo que indica que modela un agregado o contador en lugar de una entidad individual. Además, conceptos clave mencionados en los requisitos y casos de uso, como `Amistad` (CU-005, IRQ-006) o `Logro` (IRQ-005, IRQ-006), no aparecen como clases independientes, quedando implícitos o mezclados con `Objetivos` y `Usuario`.
5. **Notación UML:** Aunque se intenta estructurar la información en clases, atributos y operaciones, la mezcla de responsabilidades de diseño, casos de uso y atributos de interfaz demuestra que no se ha aplicado correctamente la notación ni el propósito de un modelo de dominio (que debe ser independiente de la implementación y la interfaz).

En conjunto, el diagrama existe y cubre gran parte de los requisitos identificados, pero su enfoque no es estrictamente conceptual y la notación presenta errores fundamentales que lo alejan de un modelo de dominio correcto.

## Puntuación
**Puntuación:** 2/10

## Observaciones
- **Eliminar clases de acción:** Retirar `Hacer ruta` y cualquier otra clase que represente un caso de uso o flujo de interacción. Sustituirlas por asociaciones entre entidades existentes (ej. `Usuario` ↔ `Ruta`).
- **Corregir atributos:** Reemplazar los booleanos de tipo “botón” por atributos de dominio reales (fechas de inicio/fin, estados, identificadores, tipos). Por ejemplo, `Ruta` debería tener `fechaInicio`, `fechaFin`, `distancia`, `estado`.
- **Modelar relaciones explícitamente:** Trasladar la información de “Operaciones” al diagrama mediante asociaciones UML con nombres de rol, direccionalidad y multiplicidades correctas (ej. `Usuario 1..* —— 0..* Ruta`, `Empresa 1 —— 0..* Árbol`).
- **Incluir clases faltantes:** Añadir `Amistad` (con atributos como `fechaCreación`, `estado`) y `Logro` (separado de `Objetivo`, con `fechaCompletado`, `tipo`), tal como exigen los requisitos IRQ-006 y CU-005.
- **Revisar granularidad:** Decidir si `Árbol` representa un ejemplar individual (sin atributo `Cantidad`) o un lote/registro de plantación. Si es individual, la cantidad se deriva de la asociación con `Usuario` o `Donación`.
- **Separar modelo de dominio de diseño:** Recordar que el modelo de dominio es conceptual y no debe incluir métodos de implementación, controles de UI ni lógica de casos de uso. Estos pertenecen al diagrama de clases de diseño o a la especificación de casos de uso.