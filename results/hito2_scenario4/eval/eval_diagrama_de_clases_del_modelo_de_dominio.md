# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento presenta el diagrama de clases del modelo de dominio en la sección 12, complementado con un glosario detallado en la sección 13. A partir de la descripción de las clases, atributos y operaciones, se pueden extraer las siguientes observaciones técnicas:

**Aciertos:**
- Se identifican las entidades conceptuales principales del dominio: `Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Empresa de plantación`, `Zona` y `Tipo de transporte`.
- Se intenta reflejar la cardinalidad de las relaciones mediante descripciones textuales en la columna de operaciones (ej. "0 o varias donaciones", "0 o muchas veces").
- La notación básica de clases (nombre, atributos, operaciones) sigue una estructura reconocible.

**Debilidades y errores conceptuales:**
1. **Confusión entre modelo de dominio y modelo de diseño/implementación:** El modelo de dominio debe representar conceptos del mundo real, no comportamientos del sistema ni elementos de interfaz. Sin embargo, se incluyen operaciones claramente funcionales/UI como `Enviar donación`, `Ver objetivos`, `Establecer objetivo`, `Hacer ruta`, o atributos como `Mantenimiento a realizar(Boolean)` y `Iniciar/Parar(Boolean)`, que corresponden a lógica de aplicación o estados de interfaz, no a propiedades conceptuales.
2. **Clases mal definidas o redundantes:** `Hacer ruta` se modela como una clase, cuando en realidad es un caso de uso o acción. Lo correcto sería una clase base `Ruta` con especialización o un atributo `tipoRuta`. Además, `Empresa de plantación` incluye `Usuario` y `Contraseña`, que son detalles de autenticación/implementación, no atributos de dominio.
3. **Clases y relaciones faltantes según los requisitos:** 
   - No aparece `Amistad` o `Relación`, esencial para el requisito IRQ-006 y el CU-005 "Competir con amigos".
   - No se modela `Logro` o `Historial`, mencionados explícitamente en IRQ-005 e IRQ-006.
   - Falta una clase `Pago` o `Transacción` para gestionar las donaciones de forma trazable.
   - Las relaciones entre clases no se representan con notación UML estándar (líneas de asociación con multiplicidades en los extremos), sino que se describen textualmente dentro de las operaciones, lo que dificulta la lectura estructural del modelo.
4. **Atributos incompletos o mal tipados:** `Árbol` contiene `Usuario (String)` y `Cantidad (Integer)`, lo que sugiere una agregación mal modelada. Un árbol debería tener atributos como `especie`, `fechaPlantación`, `estado`, y asociarse a `Usuario` y `Zona` mediante relaciones explícitas.

En conjunto, el diagrama captura la esencia del dominio y utiliza una notación comprensible, pero presenta desviaciones conceptuales significativas y omite clases/relaciones clave derivadas de la especificación de requisitos. Esto se alinea con el nivel intermedio-alto de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Separar dominio de implementación:** Eliminar atributos de seguridad (`Contraseña`), estados de interfaz (`Boolean` para botones) y operaciones de sistema (`Ver objetivos`, `Hacer ruta`). El modelo de dominio debe centrarse en *qué existe*, no en *qué hace el software*.
- **Corregir la estructura de clases:** Reemplazar `Hacer ruta` por una clase `Ruta` con generalización o un atributo enumerado. Modelar `Árbol` como entidad individual y usar asociaciones para vincularlo con `Usuario` y `Zona`.
- **Añadir clases faltantes:** Incorporar `Amistad` (con atributos como `fechaCreación`, `estado`), `Logro`/`Achievement`, y `HistorialRuta` para cubrir los requisitos de competencia y seguimiento.
- **Usar notación UML estándar:** Representar las relaciones mediante líneas de asociación con multiplicidades explícitas (ej. `Usuario "1" -- "0..*" Ruta`), evitando describirlas en la sección de operaciones.
- **Revisar atributos de dominio:** Asegurar que cada atributo represente una propiedad conceptual (ej. `Donación` debería incluir `fecha`, `monto`, `estado`, `métodoPago`, y asociarse a `Usuario` y `Empresa`).