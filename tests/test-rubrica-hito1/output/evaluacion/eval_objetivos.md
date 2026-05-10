# Evaluación: Objetivos

## Análisis
El documento define de manera clara y estructurada cuatro objetivos principales en el apartado **3.2. Objetivos**, los cuales se formalizan posteriormente en las **Tablas 1 a 4** (OBJ-001 a OBJ-004): *Rutas sostenibles*, *Plantación de árboles*, *Competencia amistosa* y *Promover la actividad física*. Cada objetivo incluye una descripción alineada con la propuesta de valor de la aplicación, un nivel de importancia (Alta) y un estado. 

Se evidencia una correcta integración en el ciclo de vida del desarrollo: los objetivos se vinculan explícitamente con los requisitos de información (IRQ), los requisitos no funcionales (NFR) y los casos de uso (CU) mediante las matrices de rastreabilidad mencionadas en el *Registro de Cambios* y reflejadas en las tablas correspondientes. Esta trazabilidad cumple con los estándares esperados en una memoria de ingeniería del software y demuestra coherencia entre la visión del producto y su especificación técnica.

No obstante, existen aspectos que limitan la puntuación máxima:
1. **Falta de métricas concretas:** Los objetivos son cualitativos y carecen de criterios SMART (específicos, medibles, alcanzables, relevantes y con plazo). No se establecen umbrales cuantificables (ej. km recorridos por árbol, tasa de conversión esperada, frecuencia de uso objetivo).
2. **Inconsistencia en el campo "Estado":** Las tablas indican `Estado: Implementado`, lo cual es incoherente con un documento de análisis y diseño donde los objetivos suelen estar en fase `Propuesto`, `Definido` o `Validado`.
3. **Originalidad limitada:** La propuesta de gamificación medioambiental vinculada al transporte sostenible es un modelo ya consolidado en el mercado (ej. WeWard, Forest, Ecosia). Aunque está bien ejecutado, no aporta un diferenciador técnico o conceptual destacado.
4. **Redundancia estructural:** El apartado **4. Objetivos** aparece vacío en el cuerpo del documento, delegando toda la información a las tablas finales, lo que genera una ligera desconexión en la lectura.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Aplicar criterios SMART:** Reformular los objetivos para incluir indicadores medibles y plazos (ej. *"Plantar 1 árbol por cada 50 km acumulados en rutas sostenibles durante el primer trimestre de uso"*).
- **Corregir el campo "Estado":** Cambiar `Implementado` por `Definido` o `Propuesto` para reflejar fielmente la fase actual del proyecto.
- **Unificar la presentación:** Completar el apartado 4 con un resumen ejecutivo de los objetivos o eliminar la sección vacía para evitar redundancias con las tablas.
- **Añadir un diferenciador:** Incluir un objetivo que destaque la propuesta única de MOVE&GROW (ej. integración con APIs de transporte público locales, verificación de impacto mediante certificaciones ambientales, o algoritmos de personalización de rutas).
- **Mantener la trazabilidad:** Continuar con la buena práctica de vincular objetivos con requisitos y casos de uso, asegurando que las matrices se actualicen automáticamente ante cambios en los objetivos.