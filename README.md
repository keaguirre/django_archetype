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
app_name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### Create virtualenv: ``` python -m venv /path/to/new/virtual/environment```
### Activate virtualenv:
- Windows: ```./virtualenv/Scripts/activate```
- Linux ```sh ./virtualenv/bin/activate```

### Deactivate virtualenv ```deactivate```