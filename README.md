# Proyecto de Integración Continua con Docker

Este proyecto implementa un entorno básico de **integración continua** utilizando **Docker**, creando y ejecutando dos contenedores que se comunican entre sí:

* **Aplicación Web** en Python (Flask)
* **Base de datos MySQL**

El objetivo es demostrar cómo contenerizar servicios y permitir que trabajen de manera conjunta mediante **Docker Compose**.

---

## 🧱 Arquitectura del Proyecto

```
┌────────────┐        ┌──────────────┐
│  Flask App │ <----> │  MySQL DB    │
└────────────┘        └──────────────┘
        |                    |
        └──── Docker Network ────┘
```

* La aplicación Flask consulta la base de datos
* La base registra el número de visitas
* Comunicación interna vía red Docker

---

## 🚀 Requisitos

Antes de ejecutar, debes tener instalado:

* Docker
* Docker Compose

---

## ▶️ Ejecución del Proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone <url-del-repo>
cd proyecto-ci
```

### 2️⃣ Construir e iniciar contenedores

```bash
docker compose up --build
```

### 3️⃣ Ver contenedores ejecutándose

```bash
docker ps
```

Deberías ver algo como:

```
proyecto-ci-web-1   Up
proyecto-ci-db-1    Up
```

### 4️⃣ Abrir la aplicación

En el navegador ingresar:

```
http://localhost:5000
```

Si la conexión es correcta, verás un mensaje como:

> Conexión a la base de datos EXITOSA. Visitas totales: X

---

## 📁 Estructura del Proyecto

```
proyecto-ci/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧪 Evidencias

* ✅ Contenedores ejecutándose (`docker ps`)
* ✅ Página web mostrando conexión exitosa a la base de datos

*(Agregar capturas de pantalla aquí)*

---

## ✅ Conclusiones

Este proyecto demuestra:

* Configuración de Multi‑Contenedores con Docker
* Comunicación entre servicios (App + Base de datos)
* Aplicación funcional ejecutada en entorno aislado

---

## 🎤 Nota para presentación

> Implementamos dos contenedores: uno con Flask y otro con MySQL. Ambos se conectan mediante Docker Compose. La app web verifica y muestra la conexión a la base de datos y el contador de visitas. Ejecutamos todo con `docker compose up --build`, simulando un ambiente real de despliegue continuo.

---

## 👨‍💻 Autor

Proyecto realizado para el curso de **Integración Continua**. Por Brian Alexander Prieto del Politecnico Gran Colombiano
