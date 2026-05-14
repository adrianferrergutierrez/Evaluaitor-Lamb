# Evaluación: Glosario de clases

## Análisis
El documento presenta un glosario de clases estructurado en las Tablas 43 a 53, cubriendo 11 clases derivadas del diagrama de clases del modelo de dominio. Se cumple con la presencia formal de los elementos solicitados (nombre, descripción, atributos y operaciones), lo que sitúa el trabajo por encima del nivel de 3/10. Sin embargo, al evaluar la calidad técnica y la corrección conceptual según los estándares de Ingeniería del Software, se identifican deficiencias críticas que impiden alcanzar el nivel de 7/10:

1. **Confusión entre Operaciones y Asociaciones**: El campo `Operaciones` no describe métodos o comportamientos de la clase, sino **relaciones estructurales y multiplicidades**. Por ejemplo, en `Usuario` se indica: `"Competir: un usuario puede competir con 0 o varios usuarios diferentes"`. En UML, esto corresponde a una asociación, no a una operación. Las operaciones deben definir la interfaz de comportamiento (ej. `registrarRuta()`, `calcularProgreso(): int`), con firmas claras, parámetros y tipos de retorno.
2. **Clases impropias para el modelo de dominio**: La clase `Hacer ruta` (Tabla 44) es un verbo/acción que corresponde a un caso de uso o a un controlador de aplicación, no a una entidad conceptual del dominio. Los modelos de dominio deben estar compuestos por sustantivos (entidades, objetos de valor, agregados).
3. **Definición deficiente de atributos**: Varios atributos presentan problemas de tipado o semántica:
   - `Iniciar (Boolean)` y `Parar (Boolean)` en `Ruta no predeterminada` son conceptualmente incorrectos; deberían ser marcas de tiempo (`Date`/`Timestamp`) o un estado enumerado.
   - `Usuario (String)` en la clase `Árbol` debería ser una referencia o identificador (`ID_Usuario`), no un tipo `String` directo.
   - `Mantenimiento a realizar(Boolean)` es ambiguo y no refleja adecuadamente la lógica de negocio.
4. **Falta de rigor en la especificación de métodos**: No se incluyen visibilidad, parámetros, tipos de retorno ni pre/postcondiciones, lo cual es esperado en un glosario técnico de nivel universitario.
5. **Coherencia con el contexto**: Aunque las clases reflejan los requisitos de información (IRQ-001 a IRQ-008) y casos de uso identificados, la traducción a clases de dominio es mecánica. No se ha aplicado una abstracción adecuada para separar la estructura de datos del flujo de interacción.

Según la rúbrica, el trabajo supera el nivel de 3/10 porque sí incluye atributos y operaciones, pero no cumple el criterio de "explicado correctamente" exigido para el 7/10. Por ello, se asigna una puntuación intermedia que refleja la presencia estructural pero la falta de corrección técnica.

## Puntuación
**Puntuación:** 5/10

## Observaciones
- **Corregir el campo "Operaciones"**: Sustituir las descripciones de relaciones/multiplicidades por métodos reales con firmas UML estándar. Ejemplo: `crearRutaPredeterminada(origen: String, destino: String, transporte: TipoTransporte): RutaPredeterminada`.
- **Eliminar clases de acción**: Suprimir `Hacer ruta` del modelo de dominio. Su lógica debe integrarse en la clase `Ruta` (como estado o servicio) o manejarse en la capa de aplicación/controladores.
- **Refinar tipos de datos y nomenclatura**: Utilizar tipos adecuados (`Date`, `Float`, `ID`, `Enum`) y evitar booleanos para representar estados complejos. Considerar una enumeración `EstadoRuta { INICIADA, EN_CURSO, FINALIZADA }`.
- **Separar estructura de comportamiento**: Documentar las asociaciones y multiplicidades en el diagrama de clases o en una sección específica de "Relaciones", manteniendo el glosario centrado en atributos (estado) y operaciones (comportamiento).
- **Alinear con los IRQ**: Revisar que cada atributo del glosario tenga correspondencia directa con los datos especificados en los Requisitos de Información (IRQ), garantizando trazabilidad y evitando redundancias o campos sin justificación funcional.