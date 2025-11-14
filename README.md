# Demo DB-per-Service

Proyecto de ejemplo donde cada microservicio usa su propia base de datos.

## Servicios

### 🟦 Users Service
- Carpeta: `service-users`
- Puerto local: **http://localhost:8001/users**
- Base de datos: **PostgreSQL**
- Contenedor DB: `users-db` (puerto expuesto 5433)

### 🟩 Products Service
- Carpeta: `service-products`
- Puerto local: **http://localhost:8002/products**
- Base de datos: **MySQL**
- Contenedor DB: `products-db` (puerto expuesto 3307)

## Ejecutar el proyecto

```bash
docker compose up -d --build
```

## Respuestas esperadas

**Users Service**
```json
{"mensaje": "Servicio de usuarios funcionando con su propia base de datos"}
```

**Products Service**
```json
{"mensaje": "Servicio de productos funcionando con su propia base de datos"}
```

## Tecnologías utilizadas
- FastAPI  
- Docker  
- PostgreSQL  
- MySQL  
