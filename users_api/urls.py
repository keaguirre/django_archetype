from django.urls import path
from .views import user_list_all, register_user, user_list_email, login_user, update_user

urlpatterns = [
    path('users/', user_list_all, name='list_all_users'),
    path('user/<str:user_email>/', user_list_email, name='user_list_by_email'),
    path('users/register/', register_user, name='register_user'),
    path('login/', login_user, name='login'),  # Ruta para la vista de login
    path('users/update', update_user, name='update_user'),
]