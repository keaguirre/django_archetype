# Django Archetype
Proyecto diseñado para prototipos, pruebas de conceptos y estudio, con el fin de hacer skip a los fundamentos afianzados e ir directo a las pruebas.

<img height="38px" src="https://skillicons.dev/icons?i=py,django,docker,postgres"/>

### Crear ambiente virtual (virtualenv):
```shell
pip install virtualenv
python -m venv /ruta/a/tu/nuevo/ambiente/virtual
```
### Activar ambiente virtual:
- Windows: `./virtualenv/Scripts/activate`
- Linux: `source ./virtualenv/bin/activate`
### Instalar paquetes:
```shell
pip install -r requirements.txt
```

### Desactivar ambiente virtual
```bash
deactivate
```

### Instalar dependencias para el proyecto:
```shell
pip install -r /path/to/requirements.txt
```

### Importar las librerias del ambiente 
```shell
pip freeze > requirements.txt
``` 
### Correr servidor local: 
```shell
python manage.py runserver
```
## .env variables required
```bash
DATABASE_URL=''
SENDGRID_API_KEY=''
FROM_MAIL=''
SECRET_KEY=''
```
## .env file variables for development Pod
### Settings.py File Database for Postgres container
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}

SENDGRID_API_KEY=''
FROM_MAIL=''
SECRET_KEY=''
```

## Docker
### Run bash in python container
```bash
docker run --name [container-name] -a stdin -a stdout -t -i [image-name] /bin/bash
```

 ### Run new container with a dev volume
```bash
docker run --name django-login -v /ruta/a/tu/app/django_login:/app -a stdin -a stdout -t -i django-login /bin/bash
```

## Obtener API Key de SendGrid
1. Ir a https://app.sendgrid.com/
1. Registrarse.
2. Crear un sender.
3. Crear la ApiKey.
4. Email API -> Integration Guide.
5. Choose WebAPI -> Python.
6. pip install sendgrid.
7. Implementar logica.

# To Do:
- [ ] Integrar nuevos modelos para endpoints standard
- [x] Integrar Django Rest Framework
- [ ] Integrar Swagger para documentar la API
- [x] Crear un docker-compose para el proyecto
- [ ] Crear un .env.example para el proyecto