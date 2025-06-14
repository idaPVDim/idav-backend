from rest_framework import serializers
from .models import CustomUser, ProfilTechnicien, ProfilClient, ProfilCommercant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'role', 'telephone', 'province']

class ProfilTechnicienSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ProfilTechnicien
        fields = ['user', 'specialite', 'certifications']

class ProfilClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ProfilClient
        fields = ['user', 'adresse', 'preferences_stockage']

class ProfilCommercantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ProfilCommercant
        fields = ['user', 'nom_boutique', 'adresse_boutique']
