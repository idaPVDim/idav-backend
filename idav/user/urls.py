from django.urls import path
from .views import UserCreateView, LoginView, UserProfileView, ProfilTechnicienView, ProfilClientView, ProfilCommercantView

urlpatterns = [
    path('register/', UserCreateView.as_view()),  # Création utilisateur (admin seulement)
    path('login/', LoginView.as_view()),          # Connexion (JWT)
    path('me/', UserProfileView.as_view()),       # Voir/modifier son profil
    path('me/technicien/', ProfilTechnicienView.as_view()),
    path('me/client/', ProfilClientView.as_view()),
    path('me/commercant/', ProfilCommercantView.as_view()),
]
