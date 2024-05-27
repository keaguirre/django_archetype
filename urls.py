from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from .views import home, login_user, register_user, logout_user, register_page


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout_user'),
    path('register_page/', register_page, name='register_page'),
    path('register_user/', register_user, name='register_user'),
]