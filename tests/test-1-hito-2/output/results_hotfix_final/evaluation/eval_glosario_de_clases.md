# Evaluación: Glosario de clases

## Análisis
El documento incluye la sección **13. Glosario de clases**, donde se presentan 11 clases mediante tablas estructuradas (Tablas 43 a 53): `Usuario`, `Hacer ruta`, `Ruta predeterminada`, `Ruta no predeterminada`, `Objetivos`, `Donaciones`, `Árbol`, `Tipo de transporte`, `Mantenimiento`, `Empresa de plantación` y `Zona`. 

Al contrastar con los niveles de la rúbrica:
- **Descripción de todas las clases:** ✅ Se listan y documentan todas las clases identificadas en el modelo de dominio.
- **Significado explicado:** ✅ Cada tabla incluye un campo `Descripción` que define claramente el propósito de la clase dentro del contexto del sistema (ej. *"Representa a las personas que utilizan la aplicación"*, *"Lugares en los que están plantados los árboles conseguidos por los usuarios"*).
- **Atributos principales:** ✅ Se detallan los atributos con sus tipos de dato correspondientes (`String`, `Boolean`, `Integer`, `Float`, etc.), cumpliendo el requisito estructural.
- **Métodos/Operaciones principales:** ⚠️ Se incluye el campo `Operaciones` en todas las tablas, pero su contenido presenta un **error conceptual recurrente**: en lugar de definir métodos o responsabilidades propias de la clase (comportamientos que la clase ejecuta), se describen **asociaciones, cardinalidades y relaciones** con otras clases (ej. *"el usuario puede enviar 0 o varias donaciones"*, *"una misma ruta predeterminada puede realizarse 0 o muchas veces"*). Esto confunde la especificación de operaciones con la definición de relaciones del modelo de dominio.

A pesar de esta desviación en la redacción de las operaciones, el glosario cumple estructuralmente con la presencia de todos los elementos exigidos por la rúbrica (clases, significado, atributos y apartado de métodos), lo que lo sitúa en el nivel de **7/10**. La puntuación no asciende a 10/10 debido a la falta de rigor en la definición de las operaciones, que no reflejan comportamientos reales ni siguen notación UML estándar.

## Puntuación
**Puntuación:** 7/10

## Observaciones
- **Reformular el campo "Operaciones":** Las operaciones deben representar métodos o responsabilidades de la clase, no multiplicidades. Se recomienda usar notación UML o descripciones funcionales claras (ej. `registrarRuta(origen, destino): void`, `calcularDistanciaAcumulada(): float`, `validarDonación(monto): boolean`).
- **Unificar nomenclatura:** En UML es convención nombrar las clases en singular (`Objetivo`, `Donación`, `RutaPredeterminada`). Se recomienda estandarizar los nombres para mantener coherencia técnica.
- **Verificar consistencia con el diagrama de clases (Sección 12):** Asegurar que cada clase, atributo y operación del glosario coincida exactamente con lo representado gráficamente en el diagrama de clases del modelo de dominio.
- **Revisar clases sin atributos:** Clases como `Hacer ruta` o `Tipo de transporte` indican "Esta clase no tiene atributos". Si son clases de control o enumeración, debe justificarse explícitamente o evaluarse si realmente pertenecen al modelo de dominio conceptual o deberían trasladarse a la capa de aplicación/diseño.