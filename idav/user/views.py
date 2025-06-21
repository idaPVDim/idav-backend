from rest_framework import viewsets, permissions, generics
from .models import CustomUser, ProfilTechnicien, ProfilClient, ProfilCommercant
from .serializers import (
    UserSerializer, ProfilTechnicienSerializer, ProfilClientSerializer, ProfilCommercantSerializer
)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserListSerializer
# Seul l'admin peut créer un utilisateur
class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

# Connexion (JWT)
class LoginView(TokenObtainPairView):
    # Utilise le serializer par défaut ou un custom si besoin
    permission_classes = [AllowAny]

# Récupérer/modifier son propre profil
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAdminUser]

  # Seuls les admins peuvent voir la liste
# Profils spécifiques
class ProfilTechnicienView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilTechnicienSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return ProfilTechnicien.objects.get(user=self.request.user)

class ProfilClientView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return ProfilClient.objects.get(user=self.request.user)

class ProfilCommercantView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilCommercantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return ProfilCommercant.objects.get(user=self.request.user)
