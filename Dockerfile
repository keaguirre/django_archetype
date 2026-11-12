# Usamos una imagen base oficial de Python
FROM python:3.13-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias primero para aprovechar la caché de capas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código del proyecto (en desarrollo, docker-compose lo monta como volumen)
COPY . .

# Exponemos el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Build Docker img:
# docker build -t django_simplest_project .
# Run bash in python container:
# docker run --name django_container -a stdin -a stdout -t -i django_simplest_project /bin/bash
