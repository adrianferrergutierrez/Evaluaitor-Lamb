# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento incluye un glosario de clases (Tablas 43 a 53) que sustenta el diagrama de clases del modelo de dominio. Aunque se han identificado las entidades principales derivadas de los requisitos funcionales e información (Usuario, Ruta, Objetivos, Donaciones, Árbol, Empresa de plantación, Zona, Mantenimiento, Tipo de transporte), el modelo presenta deficiencias estructurales y conceptuales que impiden considerarlo un modelo de dominio válido según los estándares UML y la metodología indicada:

1. **Enfoque no conceptual:** Un modelo de dominio debe representar exclusivamente conceptos del mundo real y sus relaciones, evitando detalles de implementación, interfaz o comportamiento del sistema. Sin embargo, el glosario incluye:
   - Atributos de interfaz/UI: `"Iniciar (Boolean): botón de inicio"`, `"Parar (Boolean): botón de parar"`, `"Completado (Boolean): botón para marcar..."`.
   - Detalles de seguridad/implementación: `"Contraseña"` en la clase `Empresa de plantación`.
   - Acciones modeladas como clases: `"Hacer ruta"` es un caso de uso o servicio, no una entidad conceptual. Debería existir una clase `Ruta` o `RegistroDeRuta`.
   Esto evidencia una confusión clara entre el modelo de dominio conceptual y el diseño de software o la especificación de interfaz.

2. **Uso incorrecto de la notación UML:** En un diagrama de clases de dominio, las relaciones se modelan como **asociaciones** con sus multiplicidades y roles. En este documento, las relaciones y cardinalidades se describen textualmente dentro del apartado `"Operaciones"` (ej. `"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."`). Además, un modelo de dominio conceptual **no debe incluir operaciones/métodos**, ya que estos pertenecen a la fase de diseño de software.

3. **Errores en atributos y modelado de entidades:**
   - `Árbol` incluye un atributo `Cantidad (Integer)`. Conceptualmente, una instancia de `Árbol` representa un único árbol; la cantidad debería derivarse de una agregación o de un registro histórico, no ser un atributo de la entidad.
   - `Mantenimiento` solo posee un booleano, careciendo de atributos esenciales como fecha, tipo de tarea, estado o responsable.
   - `Donaciones` incluye `Número de cuenta`, que es un dato sensible de implementación/pago, no un atributo conceptual del dominio.

4. **Elementos faltantes críticos:** A pesar de que la `"Competencia amistosa"` (OBJ-003, CU-005) y el historial de rutas/objetivos son requisitos centrales, no se modela explícitamente la relación de amistad (clase `Amistad` o asociación reflexiva en `Usuario`) ni una entidad `Historial` o `Logro` que gestione el progreso acumulado.

5. **Alineación con la rúbrica:** El modelo cumple con el nivel **2/10** (*"Se ha realizado, pero no desde un punto de vista conceptual o no se ha utilizado bien la notación"*), ya que prioriza la funcionalidad del sistema sobre la estructura conceptual del negocio y emplea una notación que mezcla asociaciones, operaciones y elementos de UI, alejándose de las buenas prácticas de modelado de dominio.

## Puntuación
**Puntuación:** 2/10

## Observaciones
- **Eliminar operaciones:** Un modelo de dominio conceptual no debe contener métodos. Retire el apartado `"Operaciones"` y modele las relaciones explícitamente como asociaciones UML con multiplicidades (ej. `Usuario 1 ─── 0..* Ruta`).
- **Corregir el enfoque conceptual:** Sustituya conceptos de interfaz/sistema (`"botón"`, `"Contraseña"`, `"Hacer ruta"`) por entidades del dominio. Por ejemplo, use `RegistroDeRuta` en lugar de `Hacer ruta`, y elimine `Contraseña` (pertenece al modelo de seguridad/diseño).
- **Revisar atributos incorrectos:** `Árbol` no debe tener `Cantidad`; si se necesita un conteo, cree una clase `ResumenDeÁrboles` o use una asociación con multiplicidad. `Mantenimiento` requiere atributos como `fecha`, `tipo`, `estado` y `observaciones`.
- **Añadir relaciones faltantes:** Modele explícitamente la amistad (`Usuario` ↔ `Usuario` con clase asociativa `Amistad` o `Seguimiento`) y un `HistorialDeActividad` o `Logro` para cubrir los requisitos de progreso y competencia.
- **Separar modelo de dominio del diseño:** Reserve las operaciones, validaciones, botones y detalles de autenticación para el modelo de diseño o los diagramas de secuencia/arquitectura. El modelo de dominio debe reflejar únicamente el vocabulario y la estructura del negocio.