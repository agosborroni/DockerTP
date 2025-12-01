# TP – Mini Plataforma Web con Persistencia y Escalabilidad

**Materia:** Entornos Virtualizados   
**Alumna:** Agostina Paz Borroni  
**Año:** 2025

---

## 1. Descripción del proyecto

Se busca  implementar una mini plataforma interna donde los empleados de una pyme hipotética puedan cargar y consultar tareas.  
La solución fue diseñada con **Docker Compose** y se compone de:

- **Backend**: API en Python (Flask)  
- **Base de datos**: PostgreSQL  
- **Admin**: Adminer para administrar la base desde el navegador  

El objetivo es demostrar persistencia (volúmenes), uso de imágenes de Docker Hub y comunicación entre servicios en una red Docker.

---

## 2. Arquitectura del sistema


| Backend | ----- | PostgreSQL | ----- | Adminer |
| Flask (5000) | | (5432) | | (8080) |
| Python 3.10 | | Imagen oficial | | UI para DB |


Todos los servicios se ejecutan dentro de la red Docker "appnet".

---

## 3. Estructura del proyecto

DockerTP/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── .env
├── docker-compose.yml
└── README.md


---

## 4. Archivos principales

### `docker-compose.yml`
Define los servicios `backend`, `db` y `adminer`.  con sus correspondientes  variables, redes, puertos y el volumen persistente.

### `.env`
Archivo con las variables de entorno utilizadas por el backend y PostgreSQL.

### `backend/Dockerfile`
Construye la imagen del backend usando la imagen oficial `python:3.10` de DockerHub.

### `backend/app.py`
API simple en Flask que prueba la conexión a PostgreSQL usando las variables de entorno.

### `backend/requirements.txt`
Lista de dependencias necesarias para ejecutarse en el contenedor.

---

##  5. Imágenes de DockerHub utilizadas

Servicio	Imagen
Backend	python:3.10
Base de datos	postgres:15
Adminer	adminer

---

## 6. Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/agosborroni/DockerTP
cd DockerTP


#### Construir y ejecutar los servicios:

docker compose up --build
Probar el backend:
http://localhost:5000/

Abrir Adminer:
http://localhost:8080/

---

## 7. Comandos útiles

docker compose up --build
docker compose down
docker logs
docker images

---

## 8. Problemas encontrados y soluciones

Docker Desktop no iniciaba por falta de virtualización, por lo que se ejecutó en GitHub Codespaces.

Variables de entorno no eran reconocidas así que  se creó archivo .env para mayor control y versatilidad.

---

## 10. Conclusión

El proyecto posee:

- Coordinación de servicios con Docker Compose
-  Uso de imágenes oficiales de Docker Hub
-  Backend en Flask
-  Base de datos PostgreSQL con persistencia
-  Administración visual por Adminer

---

Autor
Agostina Paz Borroni
EVI — 2025