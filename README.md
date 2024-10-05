# Django :snake:
### Crear ambiente virtual (virtualenv):
    pip install virtualenv
    python -m venv /ruta/a/tu/nuevo/ambiente/virtual
### Activate virtualenv:
- Windows: ```./virtualenv/Scripts/activate```
- Linux: ```source ./virtualenv/bin/activate```
  
### Desactivar ambiente virtual ```deactivate```

### Create project: 
    pip install django
    django-admin startproject mysite
### Generará algo como esto
```
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```
### Correr servidor local: 
    python manage.py runserver

## Crea un proyecto:
python manage.py startapp [app_name]
```
mysite/
├── manage.py
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── app_name/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py
```

## Variable .env From NeonDB
DATABASE_URL=''

## Docker
### Run bash in python container
 docker run --name [container-name] -a stdin -a stdout -t -i [image-name] /bin/bash

 ### Run new container with a dev volume
 docker run --name django-login -v /ruta/a/tu/app/django_login:/app -a stdin -a stdout -t -i django-login /bin/bash
