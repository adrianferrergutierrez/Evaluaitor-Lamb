# Documento de Arquitectura y Diseño - Sistema de Gestión de Biblioteca

## 1. Arquitectura General del Sistema

### 1.1 Vista Lógica

El sistema sigue una arquitectura en capas de 3 niveles:

```
┌─────────────────────────────────────┐
│     Capa de Presentación (UI)       │
│   - Web App (React)                 │
│   - Admin Dashboard                 │
└─────────────────────────────────────┘
              ↕ HTTP/REST
┌─────────────────────────────────────┐
│     Capa de Lógica de Negocio       │
│   - API Gateway                     │
│   - Servicios (Node.js/Express)     │
│   - Autenticación (JWT)             │
└─────────────────────────────────────┘
              ↕ JDBC/ORM
┌─────────────────────────────────────┐
│     Capa de Persistencia            │
│   - PostgreSQL (Datos principales)  │
│   - Redis (Cache)                   │
└─────────────────────────────────────┘
```

### 1.2 Componentes Principales

| Componente | Responsabilidad | Tecnología |
|------------|-----------------|------------|
| Frontend | Interfaz de usuario | React 18 + TypeScript |
| API Gateway | Enrutamiento y autenticación | Express.js |
| AuthService | Gestión de usuarios y JWT | Node.js |
| BookService | CRUD de libros y búsquedas | Node.js |
| LoanService | Gestión de préstamos | Node.js |
| NotificationService | Envío de notificaciones | Node.js + Nodemailer |

### 1.3 Diagrama de Contexto

```
┌──────────┐     ┌──────────────┐     ┌─────────────┐
│ Usuario  │────▶│   Sistema    │◀────│ Bibliotecario│
└──────────┘     │  Biblioteca  │     └─────────────┘
                 └──────────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │   Base de   │
                 │    Datos    │
                 └─────────────┘
```

## 2. Diagrama de Clases

### 2.1 Clases del Dominio

```
┌─────────────────────┐
│       Usuario       │
├─────────────────────┤
│ - id: UUID          │
│ - nombre: String    │
│ - email: String     │
│ - password: String  │
│ - rol: Enum         │
├─────────────────────┤
│ + login()           │
│ + logout()          │
│ + buscarLibro()     │
│ + solicitarPrestamo()│
└─────────────────────┘
         ▲
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼──────┐
│Lector │ │Biblio.  │
└───────┘ └─────────┘

┌─────────────────────┐
│        Libro        │
├─────────────────────┤
│ - isbn: String      │
│ - titulo: String    │
│ - autor: String     │
│ - categoria: String │
│ - disponible: Bool  │
├─────────────────────┤
│ + buscar()          │
│ + reservar()        │
│ + getDisponibilidad()│
└─────────────────────┘

┌─────────────────────┐
│      Prestamo       │
├─────────────────────┤
│ - id: UUID          │
│ - usuario: Usuario  │
│ - libro: Libro      │
│ - fechaInicio: Date │
│ - fechaFin: Date    │
│ - estado: Enum      │
├─────────────────────┤
│ + iniciar()         │
│ + devolver()        │
│ + renovar()         │
│ + calcularMulta()   │
└─────────────────────┘
```

### 2.2 Relaciones

- **Usuario** (1) ───── (0..*) **Prestamo**
- **Libro** (1) ───── (0..*) **Prestamo**
- **Bibliotecario** (1) ───── (0..*) **Libro** (gestión)

## 3. Diagramas de Secuencia

### 3.1 Secuencia: Registrar Préstamo

```
Bibliotecario    →   Frontend    →   API      →  LoanService  →   Database
     │                 │            │              │                │
     │─escanearLibro──▶│            │              │                │
     │                 │─POST /loans─▶│              │                │
     │                 │            │─iniciarPrestamo─▶│                │
     │                 │            │              │─verificarDisponibilidad─▶│
     │                 │            │              │                │◀───────┤
     │                 │            │              │◀───────────────┤
     │                 │            │◀─────────────┤                │
     │                 │◀───────────┤              │                │
     │◀────confirmación─│            │              │                │
```

### 3.2 Secuencia: Buscar Libro

```
Usuario    →   Frontend    →   API      →  BookService  →   Database
   │             │            │              │                │
   │─buscar(titulo)─▶│            │              │                │
   │             │─GET /books?q=─▶│              │                │
   │             │            │─buscarLibros─▶│                │
   │             │            │              │───────query──────▶│
   │             │            │              │◀────resultados────┤
   │             │            │◀─────────────┤                │
   │             │◀───────────┤              │                │
   │◀────listaLibros─│            │              │                │
```

### 3.3 Secuencia: Enviar Notificación

```
LoanService  →  NotificationService  →  EmailProvider  →  Usuario
     │                 │                    │               │
     │─eventoVencimiento─▶│                    │               │
     │                 │─prepararEmail─▶│               │
     │                 │                    │─send()────────▶│
     │                 │◀────confirmación───│               │
     │◀────notificado───│                    │               │
```

## 4. Modelo de Datos

### 4.1 Esquema de Base de Datos

```sql
-- Tabla Usuarios
CREATE TABLE usuarios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(20) DEFAULT 'lector',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla Libros
CREATE TABLE libros (
    isbn VARCHAR(13) PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    editorial VARCHAR(100),
    anio_publicacion INTEGER,
    disponible BOOLEAN DEFAULT TRUE,
    ubicacion VARCHAR(50)
);

-- Tabla Préstamos
CREATE TABLE prestamos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id UUID REFERENCES usuarios(id),
    libro_isbn VARCHAR(13) REFERENCES libros(isbn),
    fecha_inicio TIMESTAMP NOT NULL,
    fecha_fin TIMESTAMP NOT NULL,
    fecha_devolucion TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'activo',
    multa DECIMAL(10,2) DEFAULT 0
);

-- Tabla Reservas
CREATE TABLE reservas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id UUID REFERENCES usuarios(id),
    libro_isbn VARCHAR(13) REFERENCES libros(isbn),
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'pendiente'
);

-- Índices
CREATE INDEX idx_libros_titulo ON libros(titulo);
CREATE INDEX idx_libros_autor ON libros(autor);
CREATE INDEX idx_prestamos_usuario ON prestamos(usuario_id);
CREATE INDEX idx_prestamos_estado ON prestamos(estado);
```

### 4.2 Diagrama Entidad-Relación

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   Usuario   │1     *│   Prestamo  │*     1│    Libro    │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │◀──────│ usuario_id  │       │ isbn (PK)   │
│ nombre      │       │ libro_isbn  │──────▶│ titulo      │
│ email       │       │ fecha_inicio│       │ autor       │
│ password    │       │ fecha_fin   │       │ categoria   │
│ rol         │       │ estado      │       │ disponible  │
└─────────────┘       └─────────────┘       └─────────────┘
       │                      │
       │                      │
       ▼                      ▼
┌─────────────┐       ┌─────────────┐
│   Reserva   │       │ Notificacion│
├─────────────┤       ├─────────────┤
│ id (PK)     │       │ id (PK)     │
│ usuario_id  │       │ usuario_id  │
│ libro_isbn  │       │ mensaje     │
│ fecha       │       │ leida       │
│ estado      │       │ fecha       │
└─────────────┘       └─────────────┘
```

## 5. Patrones de Diseño Aplicados

### 5.1 Patrón Repository

```typescript
interface IRepository<T> {
    findById(id: string): Promise<T | null>;
    findAll(): Promise<T[]>;
    create(entity: T): Promise<T>;
    update(id: string, entity: Partial<T>): Promise<T>;
    delete(id: string): Promise<void>;
}

class LibroRepository implements IRepository<Libro> {
    private db: Database;
    
    async findById(isbn: string): Promise<Libro | null> {
        return this.db.query('SELECT * FROM libros WHERE isbn = $1', [isbn]);
    }
    
    async findAll(): Promise<Libro[]> {
        return this.db.query('SELECT * FROM libros');
    }
    
    // ... implementación completa
}
```

### 5.2 Patrón Service Layer

```typescript
class LoanService {
    private loanRepository: LoanRepository;
    private notificationService: NotificationService;
    
    async iniciarPrestamo(usuarioId: string, libroIsbn: string): Promise<Prestamo> {
        // Validaciones
        // Crear préstamo
        // Actualizar disponibilidad
        // Enviar notificación
    }
}
```

### 5.3 Patrón Observer (Notificaciones)

```typescript
interface Observer {
    update(event: PrestamoEvent): void;
}

class NotificationObserver implements Observer {
    update(event: PrestamoEvent) {
        if (event.type === 'VENCIMIENTO_PROXIMO') {
            this.enviarRecordatorio(event.usuarioId);
        }
    }
}
```

### 5.4 Patrón Factory (Autenticación)

```typescript
class AuthFactory {
    static createAuthStrategy(provider: string): AuthStrategy {
        switch(provider) {
            case 'jwt': return new JWTAuthStrategy();
            case 'oauth': return new OAuthStrategy();
            default: throw new Error('Proveedor no soportado');
        }
    }
}
```

## 6. Consideraciones Técnicas

### 6.1 Stack Tecnológico

| Capa | Tecnología | Versión | Justificación |
|------|------------|---------|---------------|
| Frontend | React | 18.x | Componentes reutilizables, gran ecosistema |
| Backend | Node.js | 20.x LTS | JavaScript full-stack, alto rendimiento I/O |
| Framework API | Express | 4.x | Ligero, flexible, maduro |
| Base de Datos | PostgreSQL | 15.x | ACID, consultas complejas, open-source |
| Cache | Redis | 7.x | Bajo latency, sesiones, colas |
| Auth | JWT | - | Stateless, escalable |

### 6.2 Escalabilidad

- **Horizontal**: Los servicios son stateless, permiten escalado horizontal
- **Load Balancer**: Nginx para distribución de carga
- **Cache**: Redis para consultas frecuentes
- **Connection Pooling**: PgBouncer para PostgreSQL

### 6.3 Seguridad

- **Autenticación**: JWT con refresh tokens
- **Encriptación**: bcrypt para contraseñas, TLS 1.3 para comunicaciones
- **Validación**: Zod para validación de inputs
- **Rate Limiting**: Express-rate-limit para prevenir abusos

### 6.4 Mantenibilidad

- **Código**: TypeScript para type-safety
- **Tests**: Jest para unit tests, Supertest para integration tests
- **Logging**: Winston para logs estructurados
- **Documentación**: Swagger/OpenAPI para la API

### 6.5 Deployment

```yaml
# docker-compose.yml (extracto)
services:
  api:
    build: ./backend
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/biblioteca
      - REDIS_URL=redis://redis:6379
  
  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
```

## 7. Métricas de Calidad

| Métrica | Objetivo | Herramienta de Medición |
|---------|----------|------------------------|
| Tiempo de respuesta API | < 200ms p95 | Prometheus + Grafana |
| Disponibilidad | 99.5% | Uptime monitoring |
| Cobertura de tests | > 80% | Jest coverage |
| Deuda técnica | < 5% | SonarQube |