# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye el apartado `12. Diagrama de clases del modelo de dominio` y el `13. Glosario de clases`, donde se detallan las entidades identificadas. Aunque el diagrama gráfico no es visible en el texto proporcionado, la evaluación se basa en la descripción textual, el glosario y la coherencia con los requisitos funcionales e información especificados.

**Aspectos positivos:**
- Se han identificado la mayoría de los conceptos clave derivados de los requisitos: `Usuario`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Empresa de plantación`, `Zona`, `Mantenimiento` y `Tipo de transporte`.
- Existe un esfuerzo claro por relacionar las clases con los casos de uso y requisitos del sistema, lo que demuestra trazabilidad con la especificación.

**Errores conceptuales y de notación:**
1. **Confusión entre acciones y entidades:** La clase `Hacer ruta` modela un caso de uso/acción, no un concepto del dominio. Los modelos de dominio deben representar sustantivos (entidades conceptuales), no verbos o flujos de interacción.
2. **Detalles de implementación en el modelo conceptual:** Atributos como `Contraseña` en `Empresa de plantación` o `Iniciar/Parar (Boolean)` en `Ruta no predeterminada` corresponden a nivel de diseño/implementación o interfaz, no al dominio conceptual.
3. **Nomenclatura incorrecta:** Las clases `Objetivos` y `Donaciones` están en plural. En UML y modelado de dominio, las clases deben nombrarse en singular.
4. **Relaciones modeladas como operaciones:** En el glosario, las asociaciones se describen dentro del apartado "Operaciones" con multiplicidades (ej. *"0 o varias donaciones"*). En un diagrama de clases UML, las relaciones deben representarse como **asociaciones** con cardinalidades en los extremos, no como métodos o comportamientos.
5. **Atributos mal conceptualizados:** En `Árbol`, el atributo `Usuario (String)` y `Cantidad (Integer)` mezclan identidad con agregación. Un árbol debería tener propiedades propias (especie, fecha de plantación, estado, coordenadas), y la relación con el usuario debe modelarse mediante una asociación, no como un atributo de tipo String.

El modelo captura el alcance funcional requerido, pero presenta errores fundamentales en la abstracción conceptual y en la aplicación de la notación UML para modelos de dominio, lo que dificulta su uso como base sólida para el diseño posterior.

## Puntuación
**Puntuación:** 3/10

## Observaciones
- **Eliminar clases de acción:** Retirar `Hacer ruta` del modelo de dominio. Las acciones deben quedar reflejadas en los casos de uso o diagramas de secuencia, no como entidades conceptuales.
- **Corregir nomenclatura:** Usar nombres en singular para todas las clases (`Objetivo`, `Donación`, `Árbol`, etc.).
- **Purar el modelo de detalles técnicos:** Eliminar atributos como `Contraseña`, `Iniciar/Parar (Boolean)` o identificadores de tipo `String` que representan claves foráneas. Estos pertenecen al modelo lógico o físico, no al conceptual.
- **Modelar relaciones correctamente:** Transformar las "operaciones" que describen vínculos en **asociaciones UML** con multiplicidades claras (ej. `Usuario "1" ── "0..*" ── Ruta`, `Empresa "1" ── "0..*" ── Árbol`).
- **Refinar atributos conceptuales:** Asegurar que cada atributo represente una propiedad real del concepto (ej. `Árbol` → `especie`, `fechaPlantacion`, `estado`; `Zona` → `coordenadas`, `clima`, `tipoSuelo`).
- **Validar con notación UML estándar:** Revisar que el diagrama gráfico utilice correctamente rectángulos de clase, compartimentos de atributos/operaciones, líneas de asociación con rombos (agregación/composición) o flechas (dependencia/herencia) según corresponda, evitando mezclar niveles de abstracción.