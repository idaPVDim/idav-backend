from django.urls import path
from .views import (
    UserCreateView, LoginView, UserProfileView,
    ProfilTechnicienView, ProfilClientView, ProfilCommercantView,
    UserListView
)

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),  # GET /user/ pour la liste
    path('register/', UserCreateView.as_view()),         # POST /user/register/
    path('login/', LoginView.as_view()),                 # POST /user/login/
    path('me/', UserProfileView.as_view()),
    path('me/technicien/', ProfilTechnicienView.as_view()),
    path('me/client/', ProfilClientView.as_view()),
    path('me/commercant/', ProfilCommercantView.as_view()),
]
