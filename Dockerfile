# Usamos una imagen base oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos Django
RUN pip install django

# Exponemos el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor de desarrollo de Django
# CMD ["django-admin", "startproject", "myproject", "."]
# Run bash in python container: docker run --name [container-name] -a stdin -a stdout -t -i [image-name] /bin/bash