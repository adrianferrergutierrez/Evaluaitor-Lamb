# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento presenta un glosario de clases (Tablas 43-53) que refleja la estructura del diagrama de clases del modelo de dominio. Se identifican entidades centrales alineadas con los objetivos y requisitos del proyecto: `Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Empresa de plantación`, `Zona` y `Tipo de transporte`. Sin embargo, el modelo presenta errores conceptuales y de notación significativos que impiden considerarlo correcto según los estándares de modelado de dominio:

1. **Confusión entre conceptos de dominio y comportamiento del sistema:** La clase `Hacer ruta` (Tabla 44) está nombrada con un verbo, lo cual corresponde a un caso de uso o acción del sistema, no a una entidad conceptual del negocio. En un modelo de dominio, las clases deben representar sustantivos.
2. **Uso incorrecto del campo "Operaciones":** En el glosario, este apartado se utiliza para describir relaciones y multiplicidades (ej. *"Usuario: el usuario puede hacer una ruta 0 o muchas veces"*), en lugar de modelar asociaciones UML explícitas con roles y cardinalidades. Esto indica una falta de comprensión de la notación para modelos conceptuales.
3. **Atributos de implementación/interfaz:** Se incluyen atributos como `Iniciar (Boolean)` y `Parar (Boolean)` en `Ruta no predeterminada`, o `Contraseña` en `Empresa de plantación`. Estos corresponden a detalles de diseño técnico o estados de UI, no a conceptos puros del dominio.
4. **Clases y relaciones faltantes según los requisitos:** El contexto de análisis muestra que los IRQ y casos de uso definen explícitamente conceptos como `Amistad`/`Amigo` (IRQ-001, CU-005), `Historial` (IRQ-005), `Logro` (IRQ-006) y `Transacción`/`Pago` (IRQ-007, CU-015). Ninguno de estos aparece como clase independiente ni está correctamente relacionado en el glosario.
5. **Falta de precisión en asociaciones:** No se especifican roles, multiplicidades ni tipos de asociación (agregación, composición, herencia) de forma clara. El Registro de Cambios menciona que el diagrama fue corregido y se añadió la clase `Zona`, lo que demuestra iteración, pero los errores estructurales persisten.

A pesar de identificar las entidades principales y realizar un esfuerzo de modelado, la confusión entre dominio y comportamiento, el uso inadecuado de la notación y la omisión de clases clave derivadas de los requisitos sitúan el trabajo en un nivel con demasiados errores conceptuales.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Unificar y renombrar clases conceptuales:** Eliminar `Hacer ruta` y fusionar `Ruta predeterminada` y `Ruta no predeterminada` en una única clase `Ruta` con un atributo `tipo` (o mediante herencia). Las clases deben ser sustantivos del negocio.
- **Modelar relaciones con notación UML correcta:** Sustituir las descripciones en "Operaciones" por asociaciones explícitas en el diagrama, indicando roles, multiplicidades (`1..*`, `0..1`, etc.) y dirección de navegación.
- **Eliminar detalles de implementación:** Retirar atributos como `Iniciar/Parar (Boolean)` o `Contraseña`. El modelo de dominio debe centrarse exclusivamente en conceptos, reglas y datos del negocio.
- **Incorporar clases faltantes derivadas de los requisitos:** Añadir `Amistad` (o relación M:N entre Usuarios), `Historial`, `Logro` y `Transacción`/`Pago` para cubrir los IRQ-001, IRQ-005, IRQ-006 e IRQ-007, y los casos de uso CU-005, CU-006 y CU-015.
- **Alinear glosario y diagrama:** Utilizar el glosario exclusivamente para documentar atributos y asociaciones. Revisar cada IRQ para asegurar que sus datos clave se reflejen como atributos o relaciones en las clases correspondientes, manteniendo una separación clara entre modelo de dominio (conceptual) y diseño de software (técnico).