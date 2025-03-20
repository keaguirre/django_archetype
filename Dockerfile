# Usamos una imagen base oficial de Python
FROM python:3.13-bullseye-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Actualizamos paquetes e instalamos git
RUN apt-get update && apt-get install -y git --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Clonamos el repositorio
RUN git clone https://github.com/keaguirre/django_simplest_project.git .

# Instalamos las dependencias de Django
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo de Django
#CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Exponemos el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Comando por defecto para iniciar el servidor de desarrollo de Django
# CMD ["django-admin", "startproject", "myproject", "."]
# Build Docker img:
# docker build -t django_simplest_project .
# Run bash in python container: 
# docker run --name django_container -a stdin -a stdout -t -i django_simplest_project /bin/bash
