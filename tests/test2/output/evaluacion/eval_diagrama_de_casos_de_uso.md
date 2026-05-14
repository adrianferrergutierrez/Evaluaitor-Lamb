# Evaluación: Diagrama de casos de uso

## Análisis
El documento hace referencia explícita al diagrama de casos de uso mediante imágenes (`img/img_*.png/jpg`) y registra en la **Tabla 1 (Registro de cambios, 19/05/2025)** que se actualizó el diagrama, corrigiendo errores de notación como la eliminación de "relaciones dobles" y la incorporación de una relación de herencia/generalización entre actores. Esto indica que el diagrama existe y que el equipo ha aplicado conscientemente la notación UML, corrigiendo desviaciones comunes.

Sin embargo, al evaluar la **definición de los casos de uso** que sustentan el diagrama, se detectan inconsistencias que impiden alcanzar la máxima puntuación:
1. **CU-010 (Gestionar comedores y refugios)**: No cuenta con una tabla de especificación completa. El documento solo incluye una nota indicando que debería dividirse en cuatro tablas CRUD, por lo que el caso de uso queda formalmente indefinido en la memoria.
2. **Errores de redacción/coherencia**: 
   - `CU-018` y `CU-019` comparten exactamente la misma descripción, lo que sugiere un error de copia-pega y dificulta distinguir la funcionalidad real de cada caso.
   - `CU-020` tiene como título "Gestionar becas y ayudas", pero su descripción hace referencia a la "gestión de usuarios registrados", generando una contradicción semántica.
3. **Precondiciones y roles**: Algunas precondiciones no se alinean con los actores definidos. Por ejemplo, en `CU-016 (Hacer donaciones)` se exige que el usuario tenga "permisos de administrador o ser responsable de voluntariados", cuando la lógica del sistema indica que cualquier usuario/voluntario autenticado debería poder donar.
4. **Notación de herencia**: El registro de cambios menciona "herencia de administrador a organizaciones benéficas". En UML, la generalización entre actores debe reflejar una relación "es un tipo de". Conceptualmente, es más coherente que `Usuario` sea la clase base y `Voluntario`, `Beneficiario` y `Administrador` hereden de él, o que `Organizaciones Benéficas` y `Administrador` sean actores independientes con roles distintos. La dirección o semántica de esta herencia podría requerir revisión para ajustarse estrictamente a la notación UML.

En conjunto, la notación del diagrama ha sido trabajada y corregida según buenas prácticas, pero la documentación textual de los casos de uso presenta vacíos y errores de coherencia que afectan la calidad global del modelado.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Completar la especificación del CU-010**: Desarrollar las cuatro tablas CRUD (Crear, Leer, Actualizar, Eliminar) para comedores y refugios, o bien unificarlo en un único caso de uso bien estructurado con flujos alternativos.
- **Revisar y corregir descripciones duplicadas o erróneas**: Diferenciar claramente `CU-018` (Buscar) de `CU-019` (Solicitar), y corregir la descripción del `CU-020` para que coincida con su título.
- **Alinear precondiciones con los actores**: Asegurar que las precondiciones reflejen correctamente los permisos y roles definidos en `ACT-001` a `ACT-004`. Por ejemplo, las donaciones no deberían requerir rol de administrador.
- **Validar la generalización de actores en el diagrama**: Revisar la relación de herencia mencionada en el registro de cambios. Se recomienda que `Usuario` actúe como actor base y que `Voluntario`, `Beneficiario` y `Administrador` hereden de él, manteniendo a `Organizaciones Benéficas` como actor externo independiente si interactúa con el sistema de forma distinta.
- **Incluir el diagrama renderizado en la entrega final**: Asegurar que las imágenes referenciadas se visualicen correctamente en el documento final para permitir una evaluación directa de la notación UML.