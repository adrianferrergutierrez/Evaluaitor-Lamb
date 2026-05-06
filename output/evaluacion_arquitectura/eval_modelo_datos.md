# Evaluación: Modelo de Datos

## Análisis por Criterio
| Criterio | Evaluación | Evidencia |
|----------|------------|-----------|
| **Normalización** | Aceptable (3NF con desnormalización controlada). El campo `disponible` en `libros` rompe la 3NF al ser un valor derivado de `prestamos` y `reservas`. Además, `autor` como `VARCHAR` limita a un único autor, lo que podría violar 1NF en casos reales. | `disponible BOOLEAN DEFAULT TRUE`<br>`autor VARCHAR(100) NOT NULL` |
| **Integridad referencial** | Parcial. Las claves foráneas están declaradas, pero carecen de reglas explícitas `ON DELETE/UPDATE`. Existe una inconsistencia crítica: la entidad `Notificacion` aparece en el diagrama ER pero no tiene definición SQL. | `usuario_id UUID REFERENCES usuarios(id)`<br>`libro_isbn VARCHAR(13) REFERENCES libros(isbn)`<br>*(Tabla `Notificacion` ausente en SQL)* |
| **Índices** | Básico pero funcional. Cubre búsquedas frecuentes por título, autor y estado. Sin embargo, faltan índices en columnas FK (`libro_isbn` en `prestamos` y `reservas`) y índices compuestos para consultas típicas (ej. `usuario_id + estado`). | `CREATE INDEX idx_libros_titulo ON libros(titulo);`<br>`CREATE INDEX idx_prestamos_usuario ON prestamos(usuario_id);` |
| **Tipos de datos** | Adecuados para el dominio. Uso correcto de `UUID`, `TIMESTAMP` y `DECIMAL(10,2)` para multas. No obstante, `rol` y `estado` usan `VARCHAR` en lugar de `ENUM` o `CHECK`, lo que permite inserción de valores inválidos. | `rol VARCHAR(20) DEFAULT 'lector'`<br>`estado VARCHAR(20) DEFAULT 'activo'`<br>`multa DECIMAL(10,2) DEFAULT 0` |
| **Diagrama ER** | Visualmente claro y muestra cardinalidades correctas (1 a *). Presenta desalineación con el esquema SQL al incluir `Notificacion` sin su tabla correspondiente y omite la representación explícita de claves foráneas en las relaciones. | `┌─────────────┐       ┌─────────────┐       ┌─────────────┐`<br>`│   Usuario   │1     *│   Prestamo  │*     1│    Libro    │`<br>`│   Notificacion│` *(solo en diagrama)* |

## Puntuación
**Puntuación:** 7/10

## Observaciones
El modelo de datos presenta una base sólida para un sistema de gestión de biblioteca, con una estructura relacional clara y un enfoque pragmático en el diseño. Sin embargo, se identifican áreas de mejora técnica y de consistencia:

1. **Consistencia entre Diagrama y SQL**: La tabla `Notificacion` está presente en el diagrama ER (Sección 4.2) pero no existe en el script SQL (Sección 4.1). Esto genera ambigüedad en la implementación y debe resolverse agregando la tabla o eliminándola del diagrama.
2. **Restricciones de Dominio**: Los campos `rol` y `estado` deberían usar `ENUM` o restricciones `CHECK` (ej. `CHECK (estado IN ('activo', 'devuelto', 'vencido'))`) para garantizar integridad a nivel de base de datos y evitar valores corruptos.
3. **Índices en Claves Foráneas**: PostgreSQL no indexa automáticamente las FK. Se recomienda agregar `CREATE INDEX idx_prestamos_libro ON prestamos(libro_isbn);` y su equivalente en `reservas` para optimizar `JOIN`s y operaciones de borrado en cascada.
4. **Desnormalización Intencional**: El campo `disponible` en `libros` es una optimización de lectura válida, pero debe mantenerse sincronizado mediante triggers o lógica de aplicación. Si no se documenta o gestiona correctamente, puede generar inconsistencias (ej. libro marcado como disponible pero con préstamo activo).
5. **Modelado de Autores/Categorías**: Para un sistema escalable, `autor` y `categoria` deberían normalizarse en tablas independientes con relaciones N:M, permitiendo múltiples autores por libro y jerarquías de categorías.

**Recomendación final**: Aplicar las correcciones de consistencia y restricciones de dominio elevaría el modelo a un nivel profesional (8.5-9/10), manteniendo su simplicidad actual pero garantizando robustez y mantenibilidad a largo plazo.