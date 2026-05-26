# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento presenta el diagrama de clases del modelo de dominio (sección 12) y su glosario correspondiente (sección 13). Aunque se identifican conceptos centrales del negocio como `Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Empresa de plantación`, `Zona` y `Tipo de transporte`, el modelo presenta errores conceptuales y estructurales significativos que limitan su validez como modelo de dominio:

1. **Confusión entre casos de uso y entidades conceptuales:** La clase `Hacer ruta` representa una acción o flujo de interacción, no un concepto del dominio. En un modelo de dominio correcto, esto debería modelarse como una clase `Ruta` con un atributo discriminador o una jerarquía de herencia.
2. **Inclusión de detalles de implementación:** Atributos como `Contraseña` en `Empresa de plantación` o `Número de cuenta` en `Donaciones` pertenecen al nivel de diseño técnico o de seguridad, no al dominio del problema. El modelo de dominio debe abstraerse de estos detalles.
3. **Modelado incorrecto de relaciones:** Las asociaciones no se representan explícitamente en el glosario ni se infieren correctamente en el diagrama. En su lugar, se describen textualmente dentro del campo "Operaciones" (ej. *"Usuario: el usuario puede hacer una ruta 0 o muchas veces"*). Además, en la clase `Árbol` se utiliza `Usuario (String)` como atributo en lugar de una asociación con la clase `Usuario`, lo que rompe el principio de modelado orientado a objetos.
4. **Conceptos faltantes según la especificación:** No se modelan entidades clave derivadas de los requisitos y casos de uso, como `Amistad`/`Amigo` (para la competencia amistosa), `Logro`/`Historial` (diferenciado de `Objetivos`), `Empleado`/`Personal` (que opera la empresa) o `Transacción`/`Pago`.
5. **Operaciones orientadas a flujos de uso:** Las operaciones listadas (ej. *"Enviar donación"*, *"Ver objetivos"*, *"Plantar árbol"*) describen pasos de casos de uso en lugar de responsabilidades conceptuales o reglas de negocio propias del dominio.

A pesar de estos fallos, el grupo demuestra un esfuerzo por identificar las entidades principales y documentar multiplicidades de forma textual. La notación UML parece seguir estándares básicos, pero el contenido conceptual no se alinea completamente con la especificación de requisitos ni con las buenas prácticas de modelado de dominio.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Eliminar `Hacer ruta` como clase:** Sustituirla por una clase `Ruta` con un atributo `tipo` (o especialización mediante herencia) que distinga entre rutas predeterminadas y espontáneas.
- **Abstraer detalles técnicos:** Retirar atributos como `Contraseña` o `Número de cuenta` del modelo de dominio. Si son necesarios, deben modelarse en el diseño de software o abstraerse a conceptos como `Credencial` o `MétodoDePago`.
- **Modelar asociaciones explícitamente:** Definir las relaciones entre clases con sus multiplicidades directamente en el diagrama y en el glosario, evitando describirlas como "operaciones". Corregir `Árbol` para que tenga una asociación con `Usuario` en lugar de un atributo de tipo String.
- **Incorporar conceptos faltantes:** Añadir clases derivadas de los requisitos funcionales, como `Amistad`, `Logro`, `HistorialDeRutas`, `Empleado` y `Transacción`.
- **Revisar las operaciones:** Enfocarlas en responsabilidades conceptuales o reglas de negocio (ej. `calcularDistancia()`, `registrarPlantación()`, `validarDonación()`) en lugar de pasos de casos de uso.
- **Mantener el enfoque conceptual:** Recordar que el modelo de dominio debe representar exclusivamente los conceptos, relaciones y reglas del negocio, dejando la interfaz, la seguridad y la persistencia para fases posteriores de diseño.