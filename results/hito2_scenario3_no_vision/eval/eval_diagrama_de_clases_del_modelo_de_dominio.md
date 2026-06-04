# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
Se ha entregado un diagrama (referenciado en las imágenes del documento) acompañado de un glosario de clases detallado (Tablas 43-53). Sin embargo, al evaluarlo bajo los estándares de un **modelo de dominio conceptual**, se identifican deficiencias estructurales y de notación significativas:

1. **Enfoque no conceptual:** Se incluye la clase `Hacer ruta`, que corresponde claramente a un caso de uso o acción del sistema, no a un concepto del dominio. Los modelos de dominio deben representar entidades del mundo real (sustantivos), no comportamientos o funcionalidades.
2. **Inclusión indebida de operaciones:** El glosario detalla operaciones para casi todas las clases (ej. `Enviar donación`, `Crear ruta predeterminada`, `Ver objetivos`, `Plantar árbol`). En un modelo de dominio conceptual, las operaciones **no se incluyen**; el foco debe estar exclusivamente en atributos y asociaciones. Esto evidencia una confusión entre modelo de dominio y diagrama de clases de diseño/implementación.
3. **Modelado de relaciones deficiente:** Las asociaciones se describen textualmente en el glosario como operaciones o multiplicidades (ej. `"Usuario: el usuario puede hacer una ruta 0 o muchas veces"`), en lugar de representarse mediante líneas de asociación UML con roles y cardinalidades en el diagrama. Además, se utilizan atributos de tipo `String` o `Integer` para representar relaciones (ej. `Usuario (String)` en la clase `Árbol`, `Cantidad (Integer)`), lo cual es incorrecto desde el punto de vista conceptual.
4. **Atributos inadecuados para el dominio:** Se incorporan atributos propios de la interfaz de usuario o del estado de ejecución (ej. `Iniciar (Boolean)`, `Parar (Boolean)`, `Completado (Boolean)`, `Contraseña`), que no pertenecen al modelo conceptual del dominio.
5. **Clases faltantes o mal definidas:** Requisitos y casos de uso mencionan conceptos como `Amistad`, `Logro`, `Historial`, `Administrador` o `Pago`, que no aparecen como clases independientes o están fusionados incorrectamente. Los nombres de clases en plural (`Objetivos`, `Donaciones`) rompen la convención UML estándar.

En conjunto, aunque se ha realizado un esfuerzo por identificar entidades clave, el modelo no sigue los principios de un diagrama de clases de dominio conceptual y la notación UML se aplica de forma inconsistente, mezclando capas de análisis, diseño e implementación. Esto se alinea directamente con el nivel **2/10** de la rúbrica.

## Puntuación
**Puntuación:** 2/10

## Observaciones
- **Corregir el enfoque conceptual:** Eliminar clases que representen acciones o casos de uso (como `Hacer ruta`). Centrarse exclusivamente en los conceptos del dominio (entidades, valores, agregados).
- **Eliminar operaciones:** Un modelo de dominio no debe incluir métodos/operaciones. Retirarlas del glosario y del diagrama.
- **Usar asociaciones UML correctas:** Representar las relaciones mediante líneas de asociación con nombres de rol y multiplicidades (ej. `Usuario "1" ── "0..*" Ruta`). Evitar usar atributos `String` o `Integer` para modelar relaciones entre clases.
- **Refinar atributos:** Eliminar flags de interfaz (`Iniciar`, `Parar`) y datos de implementación (`Contraseña`). Sustituirlos por atributos conceptuales o relaciones adecuadas.
- **Incluir conceptos faltantes:** Añadir clases como `Amistad`, `Logro`, `Historial`, `Administrador` (o usar generalización `Usuario` → `AdminTécnico`, `AdminGestión`) para cubrir los requisitos y casos de uso definidos.
- **Nomenclatura y notación:** Usar nombres de clases en singular, aplicar estereotipos `<<enumeration>>` correctamente para `Tipo de transporte`, y asegurar que el diagrama gráfico refleje fielmente las asociaciones y multiplicidades sin depender de descripciones textuales en el glosario.