# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye la sección 12 (referencia al diagrama) y la sección 13 (Glosario de clases, Tablas 43-53), lo que confirma que se ha realizado el artefacto. Sin embargo, al analizar el contenido del glosario y la estructura propuesta, se detectan deficiencias fundamentales que impiden considerarlo un modelo de dominio conceptual válido:

1. **Enfoque no conceptual:** Se incluye la clase `Hacer ruta` (Tabla 44), que corresponde claramente a un caso de uso o acción del sistema, no a una entidad del dominio. Los modelos de dominio deben representar conceptos del mundo real (sustantivos), no comportamientos o funcionalidades.
2. **Uso incorrecto de la notación UML:** En el glosario, la columna `Operaciones` se utiliza sistemáticamente para describir asociaciones y multiplicidades (ej. Tabla 43: *"Enviar donación: el usuario puede enviar 0 o varias donaciones..."*; Tabla 45: *"Creada por un usuario: una ruta predeterminada puede ser creada por uno o varios usuarios..."*). En UML, las relaciones se modelan mediante líneas de asociación con multiplicidades en los extremos, no como operaciones. Además, se listan operaciones de sistema/UI en un modelo que debería ser conceptual.
3. **Convenciones de nombrado:** Varias clases están en plural (`Objetivos`, `Donaciones`), lo cual contradice el estándar UML que exige nombres en singular.
4. **Atributos inadecuados para un modelo conceptual:** En `Ruta no predeterminada` (Tabla 46) se definen atributos como `Iniciar (Boolean)` y `Parar (Boolean)`, que son flags de interfaz o control de ejecución, no atributos de dominio. Lo conceptualmente correcto sería `fechaInicio`, `fechaFin`, `distanciaRecorrida`, `estado`.
5. **Conceptos faltantes respecto a los requisitos:** A pesar de estar explícitos en los casos de uso y requisitos de información, no se modelan clases para `Amistad`/`RelaciónSocial` (CU-005, IRQ-006), `Historial` (IRQ-005) ni `Transacción`/`Pago` (CU-015, IRQ-007), elementos centrales en la especificación.
6. **Relaciones implícitas y confusas:** Al no usar notación de asociación estándar y mezclar responsabilidades de sistema con conceptos de negocio, el diagrama resultante (inferido del glosario) carece de claridad estructural y precisión semántica.

En conjunto, el trabajo identifica conceptos relevantes del negocio, pero falla en aplicar los principios de modelado de dominio y la notación UML, ajustándose directamente a la descripción del nivel 2/10 de la rúbrica.

## Puntuación
**Puntuación:** 2/10

## Observaciones
- **Eliminar clases de comportamiento:** Retirar `Hacer ruta` y cualquier otra clase que represente un caso de uso, acción o elemento de interfaz. El modelo de dominio solo debe contener entidades conceptuales.
- **Corregir la notación de relaciones:** Utilizar líneas de asociación con multiplicidades (`1..*`, `0..1`, etc.) y roles en los extremos. No describir relaciones en la sección de operaciones.
- **Aplicar convenciones UML:** Nombrar todas las clases en singular (`Objetivo`, `Donación`, `Usuario`, `Árbol`).
- **Refinar atributos conceptuales:** Reemplazar flags de UI (`Iniciar`, `Parar`, `Completado`) por atributos de dominio como `fechaInicio`, `fechaFin`, `estado`, `distancia`, `cantidad`.
- **Incluir conceptos faltantes:** Añadir clases derivadas de los requisitos funcionales clave, como `Amistad` (o `Seguidor`), `HistorialRuta`, `HistorialObjetivo` y `Transacción`/`Pago`.
- **Separar modelo de dominio de diseño de software:** Recordar que el modelo de dominio no debe incluir operaciones de sistema, validaciones de interfaz ni detalles de implementación. Centrarse exclusivamente en los conceptos del negocio y sus relaciones naturales.