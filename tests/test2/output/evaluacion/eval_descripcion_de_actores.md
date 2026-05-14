# Evaluación: Descripción de actores

## Análisis
El documento identifica y describe cuatro actores principales mediante las tablas `ACT-001` a `ACT-004`: *Usuario registrado*, *Voluntario*, *Administrador* y *Organizaciones Benéficas*. Cada actor cuenta con una descripción funcional básica y comentarios sobre sus capacidades. Sin embargo, la evaluación revela aspectos estructurales y de coherencia que impiden alcanzar la máxima puntuación:

1. **Estructura deficiente:** La sección específica `2.3.2 Descripción de actores` aparece completamente vacía en el cuerpo del documento. Las definiciones reales se encuentran dispersas más adelante en formato de tabla, lo que rompe la trazabilidad esperada en un documento de requisitos.
2. **Inconsistencia terminológica:** Existe una discrepancia notable entre los actores definidos y el resto del modelo. El glosario (Sección 3.5) y el modelo de dominio (Tabla 50) distinguen claramente entre *Beneficiario* y *Voluntario*, pero la tabla de actores utiliza *Usuario registrado* para cubrir funciones propias de un beneficiario (solicitar becas, buscar comedores, etc.). Esta ambigüedad dificulta delimitar responsabilidades y permisos.
3. **Nivel de detalle:** Las descripciones son genéricas y no especifican precondiciones, restricciones de acceso, ni la relación explícita con los casos de uso que les corresponden. Además, el registro de cambios menciona: `"Actualizado el diagrama de casos de uso, eliminando las relaciones dobles y añadiendo la herencia de 'administrador' a 'organizaciones benéficas'"`. Esta relación de herencia es conceptualmente cuestionable en UML (una organización benéfica no es un tipo de administrador), lo que sugiere que el modelado gráfico no está optimizado.
4. **Diagrama:** Aunque se hace referencia a un diagrama de casos de uso (que incluye actores) en las secciones `2.3.3` y `3.3`, solo se muestran marcadores de imagen. La evidencia textual indica que, si bien los actores están presentes, su representación y documentación adolecen de falta de rigor y coherencia con el dominio del problema.

En conjunto, los actores están descritos, pero la organización, la consistencia terminológica y la calidad del modelado asociado no alcanzan un nivel óptimo, ajustándose al nivel intermedio de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Unificar terminología:** Reemplazar `Usuario registrado` por `Beneficiario` (o aclarar explícitamente la jerarquía de generalización) para alinearlo con el glosario y el modelo de dominio.
- **Completar la sección 2.3.2:** Incluir las definiciones oficiales en el apartado correspondiente o añadir una referencia cruzada clara a las tablas `ACT-XXX`.
- **Profundizar en las descripciones:** Añadir para cada actor: responsabilidades clave, restricciones de acceso, casos de uso principales asociados y, si aplica, justificación de relaciones de herencia/generalización.
- **Revisar el diagrama de casos de uso:** Corregir la relación de herencia entre `Administrador` y `Organizaciones Benéficas`. En UML, la herencia debe reflejar una relación "es un tipo de" válida; en este caso, sería más adecuado usar una relación de asociación o un rol compartido, no generalización.
- **Añadir trazabilidad:** Incluir una matriz o tabla que mapee explícitamente cada actor con los casos de uso que inicia o participa, mejorando la claridad y validación de requisitos.