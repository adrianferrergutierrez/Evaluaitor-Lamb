# Evaluación: Glosario de clases

## Análisis
El documento incluye la sección **13. Glosario de clases**, estructurada mediante las Tablas 43 a 53. En ella se detallan 11 clases, cubriendo íntegramente las entidades identificadas en el diagrama de clases del modelo de dominio (Usuario, Ruta predeterminada, Ruta no predeterminada, Objetivos, Donaciones, Árbol, Tipo de transporte, Mantenimiento, Empresa de plantación y Zona), añadiendo una clase adicional denominada `Hacer ruta`. 

Para cada clase se cumple con la estructura solicitada:
- **Significado:** Todas las clases cuentan con un campo `Descripción` que explica claramente su rol dentro del dominio del problema (ej. *"Representa a las personas que utilizan la aplicación"*, *"Lugares en los que están plantados los árboles..."*).
- **Atributos:** Se listan los atributos principales junto con su tipo de dato (String, Boolean, Float, Integer, etc.), cumpliendo con el requisito formal. En clases como `Hacer ruta` o `Tipo de transporte` se indica correctamente que no poseen atributos propios.
- **Métodos/Operaciones:** Se incluye el apartado `Operaciones` para todas las clases. Sin embargo, al revisar su contenido, se detecta una **confusión conceptual**: en lugar de definir métodos o comportamientos propios de la clase (con signatura, parámetros y tipo de retorno), se describen relaciones de asociación, multiplicidades o fragmentos de casos de uso (ej. *"Enviar donación: el usuario puede enviar 0 o varias donaciones..."*, *"Creada por un usuario..."*). Estas descripciones corresponden a la semántica de las asociaciones del diagrama de clases, no a operaciones de software.

A pesar de esta imprecisión técnica en las operaciones, el glosario está completo, sigue la plantilla requerida, cubre todas las clases del modelo y explica correctamente su significado y atributos, por lo que se ajusta al nivel superior de la rúbrica disponible, aunque con margen de mejora técnica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
1. **Corregir la definición de operaciones:** Transformar las descripciones actuales de relaciones/casos de uso en métodos reales con notación UML estándar. Ejemplo: cambiar `"Enviar donación: el usuario puede enviar 0 o varias donaciones..."` por `registrarDonacion(cantidad: Float, metodoPago: String): Boolean`.
2. **Eliminar redundancias conceptuales:** Las multiplicidades y asociaciones (ej. `0..*`, `1..1`) ya están representadas en el diagrama de clases. No deben repetirse en el glosario como "operaciones".
3. **Unificar nomenclatura:** Revisar la coherencia entre singular y plural (ej. `Objetivos` vs `Objetivo`, `Donaciones` vs `Donación`) para alinearlo con el diagrama de clases y las buenas prácticas de modelado.
4. **Revisar la clase `Hacer ruta`:** Esta clase parece corresponder a un caso de uso o a un controlador de interfaz, no a una entidad del dominio. Evaluar si debe mantenerse en el modelo de dominio o trasladarse a la capa de control/interfaz.