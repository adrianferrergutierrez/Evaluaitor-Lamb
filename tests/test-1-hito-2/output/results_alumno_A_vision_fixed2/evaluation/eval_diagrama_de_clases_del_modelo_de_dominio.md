# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye el diagrama de clases del modelo de dominio (sección 12) y su correspondiente glosario (sección 13, tablas 43 a 53). Aunque se identifican entidades centrales del negocio como `Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Árbol`, `Empresa de plantación`, `Zona`, `Donaciones` y `Objetivos`, el modelo presenta deficiencias conceptuales y de notación que limitan su validez como modelo de dominio conceptual:

1. **Confusión conceptual (acciones vs. entidades):** Se define la clase `Hacer ruta` (Tabla 44), la cual representa un caso de uso o comportamiento del sistema, no un concepto del dominio. Un modelo de dominio debe abstraer entidades del mundo real, no flujos de interacción.
2. **Notación incorrecta de relaciones:** Las asociaciones entre clases no se modelan mediante líneas UML con multiplicidades, sino que se describen textualmente dentro del campo `Operaciones` (ej. *"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."*). Esto desvirtúa la semántica de un diagrama de clases, donde las operaciones deben representar comportamientos propios de la entidad, no relaciones estructurales.
3. **Filtración de interfaz/implementación:** Se incluyen atributos como `Iniciar (Boolean): “botón” de inicio` (Tabla 46) o `Completado (Boolean): “botón”` (Tabla 47). Estos corresponden a elementos de UI o estados de ejecución, no a propiedades conceptuales del dominio.
4. **Nomenclatura y tipado:** Uso de nombres en plural (`Objetivos`, `Donaciones`), lo cual rompe con las convenciones de modelado. Además, la clase `Árbol` (Tabla 49) contiene un atributo `Usuario (String)` en lugar de una asociación explícita, y `Cantidad (Integer)` sugiere un agregado mal definido para una entidad que debería representar árboles individuales o lotes claramente diferenciados.
5. **Cobertura incompleta frente a requisitos:** Faltan conceptos clave derivados de los casos de uso y requisitos de información, como `Amistad`/`Competencia`, `HistorialDeRutas`/`Logro`, o `Transacción`/`Pago`. La competencia amistosa y el historial de objetivos se mencionan en los requisitos (IRQ-005, IRQ-006, CU-005) pero no se reflejan en el modelo.

En conjunto, el trabajo demuestra un esfuerzo por capturar los elementos del sistema, pero adolece de errores fundamentales en la abstracción conceptual y en la aplicación de la notación UML para modelos de dominio.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Eliminar clases de acción:** Retirar `Hacer ruta` del modelo de dominio. Las acciones deben quedar reflejadas en los diagramas de casos de uso o de secuencia, no como entidades conceptuales.
- **Modelar relaciones correctamente:** Sustituir las descripciones textuales en `Operaciones` por **asociaciones UML** con multiplicidades claras (ej. `Usuario` 1..* `Ruta`, `Usuario` *..* `Amistad`, `Empresa` 1..* `Árbol`).
- **Abstraer conceptos del negocio:** Eliminar atributos que reflejen la interfaz (`“botón”`) o estados de ejecución. Centrarse en propiedades intrínsecas (ej. `fechaInicio`, `distanciaRecorrida`, `estadoPlantación`).
- **Corregir nomenclatura y estructura:** Usar nombres de clases en **singular**. Revisar la clase `Árbol`: si representa un ejemplar, eliminar `Cantidad` y crear una asociación con `Usuario`; si representa un lote, renombrarla a `LoteDeÁrboles` o `PedidoDePlantación`.
- **Completar el modelo:** Incorporar clases faltantes derivadas de los requisitos, como `Amistad`, `Historial`, `Transacción` o `Logro`, y asegurar que todas las relaciones críticas (competencia, donaciones, mantenimiento por zona) queden explícitamente modeladas.