# Evaluación: Glosario de clases

## Análisis
El documento incluye la sección **13. Glosario de clases**, que comprende las Tablas 43 a 53. En ellas se documentan 11 clases correspondientes al modelo de dominio: `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. Cada entrada sigue una estructura uniforme que incluye: nombre de la clase, descripción de su significado, listado de atributos (con tipos de datos especificados como `String`, `Boolean`, `Float`, `Integer`) y un apartado de operaciones. Se confirma que se han cubierto todas las clases identificadas en el diagrama de dominio, incluyendo la clase `Zona` mencionada en el registro de cambios como incorporación reciente.

No obstante, se identifica un error conceptual significativo en el campo **Operaciones**: en lugar de definir métodos o comportamientos propios de la clase (con firmas, parámetros o lógica de negocio), se describen relaciones de asociación y multiplicidades con otras entidades (ej. *“el usuario puede enviar 0 o varias donaciones”*, *“0 o muchas veces”*, *“planta uno o varios árboles”*). Esto confunde las operaciones con las relaciones estructurales del diagrama de clases. A pesar de esta imprecisión, el glosario está estructuralmente completo, describe todas las clases, explica su significado y detalla sus atributos, cumpliendo así con el nivel intermedio-alto de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Corregir el apartado de Operaciones:** Reemplazar las descripciones de asociaciones/multiplicidades por métodos reales de la clase. Ejemplo: `registrarRuta()`, `calcularDistancia(): float`, `enviarDonacion(monto: float): boolean`. Incluir parámetros y tipo de retorno cuando corresponda.
- **Revisar la nomenclatura de las clases:** Algunas están en plural (`Objetivos`, `Donaciones`), lo cual no sigue la convención estándar de UML/POO. Se recomienda usar singular (`Objetivo`, `Donación`).
- **Evaluar la clase `Hacer ruta`:** Esta clase representa una acción o flujo de control más que una entidad conceptual del dominio. Considerar eliminarla del modelo de dominio o transformarla en una clase de control, integrando su lógica en `Usuario` o `Ruta`.
- **Unificar tipos de datos:** Mantener coherencia en la notación (ej. `float` vs `Float`, `String` con mayúscula inicial). Asegurar que todos los atributos tengan un tipo definido y alineado con el lenguaje de implementación previsto.
- **Añadir visibilidad (opcional pero recomendado):** Incluir modificadores de acceso (`+`, `-`, `#`) en atributos y operaciones para mayor rigor técnico y alineación con estándares UML.