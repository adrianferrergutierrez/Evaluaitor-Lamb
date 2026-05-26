# Evaluación: Diagrama de clases del modelo de dominio

## Análisis
El documento presenta un diagrama de clases del modelo de dominio (correspondiente a la descripción de `img/img_30.jpg`) que cumple con los principios básicos de un modelo conceptual, alineándose con la definición proporcionada en el glosario: *"Representación de las clases conceptuales del mundo real, no de componentes software"*. 

**Aspectos positivos:**
- **Notación UML correcta:** Se utilizan rectángulos para las clases, se especifican atributos con sus tipos de dato (`String`, `Float`, `Integer`, `Boolean`), se emplea el estereotipo `<<enumeration>>` para `Tipo Transporte` y se representan asociaciones con nombres y multiplicidades estándar (`0..*`, `0..1`, `1`).
- **Cobertura conceptual:** El diagrama identifica la mayoría de las entidades clave descritas en los requisitos y en el glosario de clases (Tablas 43-53): `Usuario`, `Donación`, `Empresa de plantación`, `Zona`, `Árbol`, `Objetivo`, `Ruta Predeterminada`, `Ruta no predeterminada` y `Tipo Transporte`.
- **Separación de responsabilidades:** Se evita incluir operaciones o lógica de software, manteniendo el foco en la estructura estática del dominio, lo cual es adecuado para esta fase del modelado.

**Aspectos a mejorar / Inconsistencias:**
- **Relaciones conceptualmente débiles:** La asociación `Donación → Ruta Predeterminada` (0..*) no se justifica en la especificación. Según los objetivos y requisitos, las donaciones financian la plantación de árboles a través de empresas, no la creación de rutas. Esta relación parece forzada o mal interpretada.
- **Falta de generalización:** `Ruta Predeterminada` y `Ruta no predeterminada` comparten atributos y comportamientos implícitos. En un modelo de dominio robusto, deberían heredar de una clase base `Ruta` para evitar duplicidad y reflejar mejor la semántica del dominio.
- **Clases omitidas:** El glosario define explícitamente la clase `Mantenimiento` (Tabla 51) con sus atributos y operaciones, pero esta no aparece en el diagrama de clases, rompiendo la trazabilidad con la especificación.
- **Multiplicidades y roles:** Algunas asociaciones carecen de nombres de rol claros o presentan multiplicidades discutibles según los casos de uso. Por ejemplo, la relación entre `Ruta no predeterminada` y `Objetivo` (0..*) no queda clara en la lógica de negocio descrita (los objetivos suelen estar asociados al `Usuario`, no directamente a una ruta espontánea).

En conjunto, el diagrama demuestra un buen dominio de la notación UML y un enfoque conceptual adecuado, pero presenta desviaciones respecto a la lógica de negocio definida en los requisitos y omite elementos clave documentados en el propio glosario.

## Puntuación
**Puntuación:** 7/10

## Observaciones
1. **Incorporar herencia:** Crear una clase abstracta o base `Ruta` de la que hereden `RutaPredeterminada` y `RutaNoPredeterminada`, trasladando atributos comunes (origen, destino, tipo de transporte, distancia, etc.).
2. **Revisar asociaciones:** Eliminar o justificar la relación `Donación → Ruta Predeterminada`. En su lugar, reforzar la trazabilidad `Donación → Empresa de plantación` y `Empresa → Árbol/Zona`, que es el flujo real descrito en los objetivos.
3. **Incluir clases faltantes:** Añadir la clase `Mantenimiento` al diagrama, vinculándola correctamente con `Zona` y `Empresa de plantación`, tal como se detalla en el glosario (Tabla 51).
4. **Ajustar multiplicidades y roles:** Revisar las cardinalidades a la luz de los casos de uso (ej. `CU-002 Hacer ruta`, `CU-004 Configurar objetivos`) y añadir nombres de rol en las asociaciones para mejorar la legibilidad semántica (ej. `usuarioRealiza`, `empresaMantiene`).
5. **Validar contra la matriz de requisitos:** Cruzar cada clase y relación con la matriz de objetivos-requisitos y el glosario para garantizar que no haya elementos huérfanos ni relaciones sin justificación funcional.