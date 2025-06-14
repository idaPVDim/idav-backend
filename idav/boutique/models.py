from django.db import models

# Create your models here.
from django.db import models
from user.models import ProfilCommercant

class Marque(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='marques/logos/', null=True, blank=True)
    def __str__(self):
        return self.nom

class Specification(models.Model):
    TYPE_VALEUR = [
        ('entier', 'Entier'),
        ('decimal', 'Décimal'),
        ('texte', 'Texte'),
    ]
    nom = models.CharField(max_length=100)
    unite = models.CharField(max_length=50, blank=True)
    type_valeur = models.CharField(max_length=10, choices=TYPE_VALEUR)
    def __str__(self):
        return f"{self.nom} ({self.unite})" if self.unite else self.nom

class TypeEquipement(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    specifications = models.ManyToManyField(Specification)
    def __str__(self):
        return self.nom

class Boutique(models.Model):
    nom = models.CharField(max_length=100)
    commercant = models.ForeignKey(ProfilCommercant, on_delete=models.CASCADE, related_name='boutiques')
    adresse = models.TextField(blank=True)
    def __str__(self):
        return self.nom

class Equipement(models.Model):
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE, related_name='equipements')
    marque = models.ForeignKey(Marque, on_delete=models.SET_NULL, null=True, blank=True)
    type_equipement = models.ForeignKey(TypeEquipement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    puissance_nominale = models.DecimalField(max_digits=8, decimal_places=2)
    tension_nominale = models.DecimalField(max_digits=8, decimal_places=2)
    prix_reference = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    saisie_manuelle = models.BooleanField(default=False)
    valeurs_specs = models.JSONField(default=dict, blank=True)
    def __str__(self):
        return f"{self.nom} ({self.boutique.nom})"

class EquipementImage(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='equipement_images/')
    def __str__(self):
        return f"Image for {self.equipement.nom}"
