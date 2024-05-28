# Django

### Create project: 
    pip install django
    pip install virtualenv
    django-admin startproject [mysite]
```
 mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
### Correr servidor local: 
```python manage.py runserver```

## Create an App:
python manage.py startapp [app_name]
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    app_name/
        __init__.py
        admin.py
        apps.py
        migrations/
        models.py
        tests.py
        views.py
```

### Create virtualenv: ``` python -m venv /path/to/new/virtual/environment```
### Activate virtualenv:
- Windows: ```./virtualenv/Scripts/activate```
- Linux ```sh ./virtualenv/bin/activate```

### Deactivate virtualenv ```deactivate```

## Docker
### Run bash in python container
 docker run --name [container-name] -a stdin -a stdout -t -i [image-name] /bin/bash

 ### Run new container with volume
 docker run --name django-login -v /mnt/c/Users/kevin/OneDrive/Escritorio/django_login:/app -a stdin -a stdout -t -i django-login /bin/bash
