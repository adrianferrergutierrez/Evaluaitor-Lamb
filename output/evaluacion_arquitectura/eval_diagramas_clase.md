# Evaluación: Diagramas de Clases

## Análisis por Criterio
| Criterio | Evaluación | Evidencia |
|----------|------------|-----------|
| Completitud | Parcial. Se incluyen atributos y métodos, pero faltan firmas completas (parámetros y tipos de retorno). Además, hay inconsistencias con el esquema de BD (ej. `multa` y `fecha_devolucion` en `Prestamo` aparecen en la tabla SQL pero no en la clase). | Sección 2.1 (métodos como `+ login()` sin parámetros) vs Sección 4.1 (esquema SQL con campos adicionales en `prestamos`). |
| Relaciones | Deficiente en representación visual. La herencia está bien indicada, pero las asociaciones entre `Prestamo`, `Usuario` y `Libro` solo se describen textualmente. No hay líneas de conexión ni multiplicidades en el diagrama ASCII. | Sección 2.1 (diagrama sin líneas de asociación) y Sección 2.2 (descripción textual de cardinalidades `1 ───── 0..*`). |
| Notación | Básica pero funcional. Usa compartimentos estándar y modificadores de visibilidad (`-`, `+`), pero omite tipos precisos (`Enum`, `Bool` en lugar de `Boolean` o nombres concretos) y no sigue la sintaxis UML completa para operaciones. | Sección 2.1 (uso de `▲` para herencia, `-id: UUID`, `+buscarLibro()`). |
| Cohesión | Baja/Moderada. Las entidades mezclan datos de dominio con lógica de negocio y casos de uso. Métodos como `login()`, `buscarLibro()` o `reservar()` deberían residir en la capa de servicios, no en las entidades. | Sección 2.1 (métodos en `Usuario` y `Libro`) vs Sección 5.2 (declaración explícita de patrón Service Layer). |
| Acoplamiento | Moderado. `Prestamo` referencia directamente a `Usuario` y `Libro`, lo cual es aceptable, pero la lógica dispersa en las entidades genera acoplamiento conceptual innecesario. La arquitectura en capas mitiga esto, pero el diagrama no lo refleja. | Sección 2.1 (atributos `usuario: Usuario`, `libro: Libro` en `Prestamo`) y Sección 1.1 (arquitectura en capas). |

## Puntuación
**Puntuación:** 6.5/10

## Observaciones
El diagrama de clases presentado cumple una función descriptiva inicial, pero presenta varias áreas de mejora técnica y de modelado:

1. **Alineación con la Arquitectura Declarada:** El documento establece explícitamente un patrón *Service Layer* (Sección 5.2) y una arquitectura en capas. Sin embargo, el diagrama de clases asigna responsabilidades de servicio (`login()`, `buscarLibro()`, `calcularMulta()`) directamente a las entidades de dominio. Esto genera un modelo híbrido confuso. Se recomienda mantener las clases de dominio como *anémicas* (solo datos y validaciones básicas) o, si se opta por un *Rich Domain Model*, justificar claramente la distribución de responsabilidades y eliminar la redundancia con la capa de servicios.

2. **Precisión en la Notación UML:** Aunque el formato ASCII es válido para documentación ágil, carece de rigor UML. Las operaciones deben incluir firma completa: `+ nombre(parámetros): tipoRetorno`. Además, los tipos `Enum` y `Bool` son ambiguos; se sugiere usar `Boolean` y especificar el nombre del enumerador (ej. `RolUsuario`, `EstadoPrestamo`).

3. **Representación de Relaciones:** La sección 2.2 describe correctamente las cardinalidades, pero el diagrama visual (2.1) no las integra. En UML, las asociaciones deben dibujarse con líneas que conecten las clases, indicando multiplicidades en los extremos (ej. `1` en `Usuario`, `0..*` en `Prestamo`). La relación `Bibliotecario` → `Libro` (gestión) tampoco se visualiza en el diagrama.

4. **Consistencia con el Modelo de Datos:** Existen discrepancias entre el diagrama de clases y el esquema SQL (Sección 4.1). Por ejemplo, `Prestamo` en la BD incluye `fecha_devolucion` y `multa`, atributos críticos para la lógica de negocio que faltan en la clase. Se recomienda sincronizar ambos artefactos antes de la implementación.

**Recomendaciones de mejora:**
- Refactorizar el diagrama para separar claramente *Entidades de Dominio* (datos) de *Servicios* (lógica de negocio).
- Añadir firmas completas a los métodos y tipos de datos específicos.
- Dibujar las líneas de asociación con multiplicidades directamente en el diagrama ASCII o migrar a una herramienta UML estándar.
- Alinear atributos de clases con el esquema relacional para evitar inconsistencias y facilitar el mapeo ORM.