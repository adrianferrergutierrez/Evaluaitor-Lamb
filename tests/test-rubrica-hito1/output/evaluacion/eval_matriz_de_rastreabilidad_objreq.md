# Evaluación: Matriz de rastreabilidad: obj-req

## Análisis
En el documento proporcionado, la sección `## 10. Matriz de objetivos con requisitos` aparece vacía en el texto extraído, lo que indica probablemente que se trata de una imagen o tabla que no se renderizó en la conversión. No obstante, la rastreabilidad entre objetivos y requisitos está **completa y correctamente implementada** a lo largo de la documentación. 

Cada tabla de requisito de información (IRQ-001 a IRQ-008) y requisito no funcional (NFR-001 a NFR-009) incluye un campo explícito `Objetivos asociados` donde se vincula con uno o varios de los cuatro objetivos definidos (OBJ-001 a OBJ-004). Además, el `Registro de Cambios` confirma explícitamente: *"Hemos modificado la matriz de objetivos-requisitos, para que todos estén relacionados con los objetivos. Atendiendo a esta matriz los objetivos han sido añadidos correctamente a las tablas de los requisitos y los casos de uso."*

Tras verificar la coherencia de las asociaciones:
- **Todos los requisitos** (8 IRQ y 9 NFR) están vinculados a al menos un objetivo. No existen requisitos huérfanos.
- Las relaciones son lógicas y alineadas con la descripción del proyecto (ej. IRQ-002/003 → OBJ-001 Rutas sostenibles; IRQ-007/008 → OBJ-002 Plantación de árboles; NFR-006/009 → todos los objetivos por su carácter transversal).
- La misma estructura de trazabilidad se aplica consistentemente en las tablas de casos de uso.

Por tanto, el criterio se cumple satisfactoriamente y se ajusta al nivel máximo de la rúbrica.

## Puntuación
**Puntuación:** 10/10

## Observaciones
- **Visibilidad de la matriz consolidada:** Asegurar que la tabla explícita de la Sección 10 se incluya y visualice correctamente en la entrega final. Una matriz en formato de cuadrícula (Objetivos vs. Requisitos) facilita la validación rápida y evita depender únicamente de la revisión tabla por tabla.
- **Consistencia con casos de uso:** Verificar que la matriz consolidada también refleje la relación con los casos de uso, tal como se menciona en el registro de cambios, para ofrecer una visión unificada de la trazabilidad completa (Obj → Req → CU).
- **Documentación del criterio de asociación:** Añadir una breve nota metodológica que explique cómo se decidió la vinculación (ej. criterios de impacto, prioridad o cobertura funcional), lo que reforzaría la trazabilidad desde una perspectiva de ingeniería de requisitos formal.