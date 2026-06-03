# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El modelo de dominio se presenta principalmente a través del glosario de clases (Tablas 43 a 53) y se referencia visualmente en la sección 12. Su evaluación se basa en la coherencia conceptual, la notación implícita, la cobertura de requisitos y la adherencia a los principios de modelado de dominio:

1. **Cobertura de requisitos y objetivos**: El modelo identifica las entidades principales derivadas de los requisitos funcionales: `Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Empresa de plantación`, `Zona` y `Mantenimiento`. Esto demuestra un buen trabajo de elicitación y una estructura base alineada con los objetivos OBJ-001, OBJ-002 y OBJ-004.
2. **Errores conceptuales significativos**:
   - **`Hacer ruta` como clase**: Se modela una acción/caso de uso como una clase de dominio. En un modelo conceptual, las acciones no deben ser clases; deberían representarse como asociaciones o eliminarse, dejando `Ruta` como entidad central con un atributo o especialización para el tipo.
   - **Operaciones de nivel de sistema**: Las columnas de "Operaciones" en el glosario describen funcionalidades de interfaz o casos de uso (`Enviar donación`, `Ver objetivos`, `Realizar donación`, `Plantar árbol`). Un modelo de dominio debe centrarse en responsabilidades conceptuales y reglas de negocio, no en operaciones de software.
   - **Atributos mal tipados**: En la clase `Árbol`, el atributo `Usuario (String)` rompe el principio de asociación conceptual. Debería ser una relación con la clase `Usuario`. Asimismo, `Cantidad (Integer)` sugiere un agregado o resumen, no una instancia individual de árbol.
   - **Mezcla de dominio y diseño**: Atributos como `Contraseña` en `Empresa de plantación` pertenecen a la capa de seguridad/diseño, no al dominio conceptual.
3. **Clases y relaciones faltantes**: El objetivo OBJ-003 (`Competencia amistosa`) y el requisito IRQ-001 mencionan explícitamente la gestión de amistades y la compartición de logros. No existe ninguna clase `Amistad`, `Seguidor` o `Competencia` que modele esta relación muchos-a-muchos, ni una clase `Historial` o `Logro` diferenciada de `Objetivos`, a pesar de ser requisitos clave.
4. **Notación**: Aunque no se visualiza directamente la imagen del diagrama, el glosario sigue una estructura tabular que refleja una intención de notación UML. Sin embargo, la cardinalidad y los roles de las asociaciones se describen textualmente en las operaciones, lo que indica que el diagrama visual probablemente carece de una representación clara de multiplicidades y roles en las líneas de asociación.

En conjunto, el modelo está bien planteado en cuanto a identificación de entidades principales, pero presenta **demasiados errores conceptuales** propios de una confusión entre modelo de dominio, diseño de software y especificación de casos de uso. Esto lo sitúa en el nivel que describe la rúbrica para modelos con estructura base pero con fallos sustanciales en la abstracción conceptual.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Eliminar clases de acción**: Retirar `Hacer ruta` del modelo. Unificar `Ruta predeterminada` y `Ruta no predeterminada` bajo una clase general `Ruta` con un atributo `tipo` o mediante herencia, y modelar la relación con `Usuario` mediante una asociación con multiplicidad adecuada.
- **Corregir operaciones**: Reemplazar las operaciones de tipo caso de uso por responsabilidades de dominio conceptuales (ej. `calcularDistancia()`, `registrarMantenimiento()`, `actualizarEstado()`). Si no son necesarias para el modelo conceptual, pueden omitirse.
- **Modelar relaciones faltantes**: Añadir una clase `Amistad` o `RedSocial` que relacione `Usuario` consigo mismo (asociación reflexiva) para cubrir OBJ-003. Diferenciar `Objetivo` (meta futura) de `Logro` (objetivo cumplido) si la lógica de negocio lo requiere.
- **Usar asociaciones en lugar de atributos primitivos**: Cambiar `Usuario (String)` en `Árbol` por una asociación `1..*` hacia `Usuario`. Hacer lo mismo para `Empresa de plantación` y `Zona` donde corresponda.
- **Separar dominio de diseño**: Eliminar atributos de infraestructura/seguridad (`Contraseña`, `Número de cuenta`) del modelo de dominio. Estos pertenecen al modelo de diseño o a la capa de persistencia.
- **Refinar notación UML**: Asegurar que el diagrama visual muestre claramente las multiplicidades (`1`, `0..*`, `1..*`), los roles de asociación y, si aplica, clases de enumeración (`TipoTransporte`) con la notación `<<enumeration>>`.