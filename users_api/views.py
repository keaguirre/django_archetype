import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django_login.sendgrid_mails import send_email
load_dotenv()
@api_view(['GET'])
def user_list_all(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response (status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def user_list_email(request, user_email):
    """Obtiene un usuario por su email"""
    try:
        user = User.objects.get(email=user_email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        # Usamos el serializer para validar los datos recibidos
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Guardamos el usuario, lo que también cifra la contraseña
            user = serializer.save()
            
            # Obtenemos el email desde validated_data
            email = serializer.validated_data['email']
            
            # Parámetros para el correo
            from_mail = os.getenv('FROM_MAIL')  # Asumo que tienes configurado tu correo de envío en las variables de entorno
            to_email = email
            mail_subject = 'Registro exitoso'
            mail_content = f'Hola, {email}, te has registrado con éxito en nuestra plataforma.'
            
            # Llamamos a la función que enviará el correo
            send_email(from_mail, to_email, mail_subject, mail_content)
            
            # Respondemos con un mensaje de éxito
            return Response({"message": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        
        # Si el serializer no es válido, devolvemos los errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Si no es una petición POST, devolvemos un error 405
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def login_user(request):
    """Autentica a un usuario usando el sistema de autenticación de Django y crea una sesión"""
    
    # Obtener los datos del request (usuario y contraseña)
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({"error": "El nombre de usuario y la contraseña son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Autenticar al usuario
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        # Si la autenticación es exitosa, logueamos al usuario
        login(request, user)
        return Response({"message": "Autenticación exitosa"}, status=status.HTTP_200_OK)
    else:
        # Si no es válido, respondemos con error
        return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PATCH'])  # Usamos PATCH para actualizaciones parciales
def update_user(request):
    """Actualiza el username y el email del usuario autenticado"""
    # Verificamos que el usuario esté autenticado
    if not request.user.is_authenticated:
        return Response({"detail": "No autenticado."}, status=status.HTTP_401_UNAUTHORIZED)

    # Obtenemos el usuario actual
    user = request.user

    # Verificamos si 'username' o 'email' fueron enviados en la solicitud
    username = request.data.get('username', None)
    email = request.data.get('email', None)

    # Si no se envían ninguno de los dos campos, devolvemos un error
    if not username and not email:
        return Response({"detail": "Se debe proporcionar al menos un campo a actualizar."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Actualizamos el username si se ha enviado uno nuevo
    if username:
        user.username = username

    # Actualizamos el email si se ha enviado uno nuevo
    if email:
        # Validamos que el email no esté en uso por otro usuario
        if User.objects.filter(email=email).exists():
            return Response({"detail": "Este correo electrónico ya está en uso."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        user.email = email

    # Guardamos los cambios en la base de datos
    user.save()

    # Serializamos el usuario actualizado y devolvemos los datos
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])# Toma las creds del usuario desde las cookies (request.user) y cierra la sesión
@permission_classes([IsAuthenticated])  # Asegura que el usuario esté autenticado
def logout_user(request):
    """Cerrar sesión del usuario autenticado"""
    
    if request.user.is_authenticated:
        logout(request)
        return Response({"message": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "No hay usuario autenticado"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Asegura que el usuario esté autenticado
def protected_view(request):
    return Response({"message": "¡Acceso autorizado!"}, status=status.HTTP_200_OK)