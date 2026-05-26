# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento presenta el diagrama de clases del modelo de dominio en la sección 12 y su glosario correspondiente en la sección 13 (tablas 43 a 53). Tras revisar la especificación, se identifican las siguientes evidencias:

1. **Enfoque no conceptual:** Un modelo de dominio debe representar entidades y conceptos del mundo real, independientemente de la implementación. Sin embargo, el documento incluye clases que representan acciones o flujos de casos de uso, como `Hacer ruta`, lo cual es incorrecto en un modelo conceptual. Además, el campo "Operaciones" de cada clase describe comportamientos del sistema o pasos de casos de uso (ej. `"Enviar donación"`, `"Competir"`, `"Plantar árbol"`, `"Proceso de plantación"`) en lugar de responsabilidades intrínsecas del dominio.
2. **Notación UML deficiente:** Las relaciones y multiplicidades no se representan mediante la notación gráfica estándar de UML (líneas de asociación con cardinalidades `0..*`, `1..1`, etc.). En su lugar, se describen textualmente dentro del glosario bajo "Operaciones" (ej. `"Usuario: el usuario puede hacer una ruta 0 o muchas veces..."`). Los atributos carecen de modificadores de visibilidad (`+`, `-`, `#`) y algunos tipos son informales o redundantes.
3. **Cobertura y coherencia con requisitos:** Aunque se identifican conceptos alineados con los requisitos (`Usuario`, `Ruta predeterminada`, `Árbol`, `Empresa de plantación`, `Zona`, `Donaciones`), faltan entidades clave derivadas de los casos de uso y requisitos, como `Amistad`/`Competencia`, `HistorialDeRutas` o `Transacción/Pago`. La clase `Árbol` incluye un atributo `Usuario (String)` que rompe la modelización conceptual y debería resolverse mediante una asociación. La clase `Tipo de transporte` se define como enumeración pero se modela como clase vacía, lo cual es innecesario.
4. **Conclusión:** El trabajo identifica los elementos principales del dominio, pero la ejecución se aleja de los principios de modelado conceptual y no aplica correctamente la notación UML, cumpliendo con los criterios de la puntuación baja definida en la rúbrica.

## Puntuación
**Puntuación:** 2/10

## Observaciones
- **Eliminar clases de acción:** Sustituir `Hacer ruta` por una entidad conceptual `Ruta` que utilice herencia o un atributo discriminador para diferenciar entre rutas predeterminadas y espontáneas.
- **Aplicar notación UML estándar:** Representar todas las asociaciones, agregaciones y composiciones gráficamente en el diagrama, indicando las multiplicidades en los extremos de las líneas. El glosario debe limitarse a describir atributos y, si es necesario, operaciones de dominio puras.
- **Separar dominio de sistema:** Retirar del modelo de dominio las operaciones que describen flujos de casos de uso o interacciones con el sistema. El modelo de dominio solo debe contener atributos y relaciones conceptuales.
- **Incorporar conceptos faltantes:** Añadir clases como `Amistad`, `Historial` o `Transacción` para cubrir los requisitos de competencia amistosa, registro de rutas y gestión de donaciones. Resolver referencias cruzadas (ej. `Usuario` en `Árbol`) mediante asociaciones explícitas.
- **Revisar tipificación y visibilidad:** Aplicar modificadores de visibilidad UML y estandarizar los tipos de datos (ej. `String`, `Integer`, `Float`, `Boolean`, `Date`).