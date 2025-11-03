# Imagen base de Python
FROM python:3.10-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir flask mysql-connector-python

# Exponer puerto de la aplicación
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
