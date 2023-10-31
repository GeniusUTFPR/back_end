from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import (
    UsuarioSerializer,
    UsuarioDetailSerializer,
)

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_serializer_class(self):
        if self.action == "list":
            return UsuarioDetailSerializer
        elif self.action == "retrieve":
            return UsuarioDetailSerializer
        return UsuarioSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Extraia a senha da solicitação
            senha = serializer.validated_data['password']

            # Crie o usuário
            user = Usuario.objects.create(
                email = serializer.validated_data['email'],
                nome = serializer.validated_data['nome'],
                registro = serializer.validated_data['registro'],
                curso = serializer.validated_data['curso'],
            )

            # Criptografe a senha explicitamente
            user.set_password(senha)
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
