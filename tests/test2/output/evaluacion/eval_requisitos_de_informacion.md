# Evaluación: Requisitos de información

## Análisis
El documento define los requisitos de información mediante las tablas `IRQ-001` a `IRQ-008`, que cubren las entidades principales del sistema: Perfil, Donaciones, Ayuda, Comedores, Refugios, Historial de voluntariados, Voluntariado y ONG. Cada tabla sigue una estructura formal que incluye descripción, datos específicos, tiempo de vida, ocurrencias simultáneas, importancia, urgencia, estado, estabilidad y trazabilidad con objetivos y otros requisitos.

Sin embargo, se identifican varias deficiencias que impiden alcanzar la máxima puntuación:
1. **Estructura vacía en la sección principal**: Los apartados `2.2.1 Requisitos de almacenamiento de la información` y `2.2.2 Requisitos de restricción de la información` aparecen completamente vacíos en el cuerpo del documento. Las tablas IRQ se encuentran más adelante sin una integración jerárquica clara.
2. **Errores de copia y pega**: Las tablas `IRQ-004 (Comedores)` y `IRQ-005 (Refugios)` contienen exactamente la misma descripción y los mismos "Datos específicos", lo que indica una falta de revisión y diferenciación técnica entre dos entidades distintas.
3. **Información faltante respecto a los casos de uso**: Varios datos explícitamente mencionados en los casos de uso no aparecen en los requisitos de información correspondientes. Por ejemplo:
   - `CU-018` y `CU-019` mencionan el uso del **DNI** y el **grado de vulnerabilidad** para filtrar becas/ayudas, pero `IRQ-003` no los incluye en sus datos específicos.
   - `CU-008` hace referencia a la **geolocalización/coordenadas** para el mapa interactivo, ausente en `IRQ-004` e `IRQ-005`.
   - `CU-016` detalla validación de tarjeta y gestión de pagos, pero `IRQ-002` solo lista "Datos de pago" de forma genérica sin especificar tokens, fechas de expiración o estados de transacción.
4. **Falta de precisión técnica**: Los "Datos específicos" se presentan como listas planas sin indicar tipos de datos, restricciones de formato, claves primarias/foráneas o relaciones entre entidades, lo que limita su utilidad para el diseño de la base de datos.

A pesar de estos fallos, los requisitos están formalmente definidos, cubren los dominios de información principales del sistema y mantienen una trazabilidad básica con los objetivos y casos de uso, lo que se ajusta al nivel intermedio de la rúbrica.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Integrar correctamente las tablas IRQ** en la sección `2.2` o rellenar los apartados `2.2.1` y `2.2.2` con la documentación correspondiente para mantener la coherencia estructural del documento.
- **Corregir la duplicación entre IRQ-004 e IRQ-005**, diferenciando claramente los datos propios de comedores (ej. tipo de comida, horarios, capacidad diaria) y refugios (ej. tipo de alojamiento, duración máxima de estancia, normas de acceso).
- **Realizar un cruce exhaustivo con los casos de uso** para asegurar que todos los campos de datos mencionados en los flujos normales y excepciones (DNI, grado de vulnerabilidad, coordenadas GPS, estados de reserva, tokens de pago, etc.) queden reflejados en los `Datos específicos` de cada IRQ.
- **Añadir especificaciones técnicas** a los datos: tipos (string, integer, date, boolean), restricciones (longitud, formato, obligatoriedad), y relaciones entre entidades para facilitar la transición al modelo de dominio y al diseño de la base de datos.
- **Actualizar las matrices de rastreabilidad** para incluir explícitamente la relación `IRQ ↔ CU`, garantizando que ningún dato de los casos de uso quede sin cubrir en los requisitos de información.