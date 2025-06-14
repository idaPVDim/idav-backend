from django.db import models
from user.models import ProfilClient, ProfilTechnicien
from boutique.models import Equipement

class Installation(models.Model):
    client = models.ForeignKey(ProfilClient, on_delete=models.CASCADE, related_name='installations')
    technicien = models.ForeignKey(ProfilTechnicien, on_delete=models.SET_NULL, null=True, blank=True, related_name='installations')
    consommation_energetique = models.DecimalField(max_digits=12, decimal_places=2)
    province = models.CharField(max_length=100)
    option_stockage = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    equipements = models.ManyToManyField(Equipement, through='InstallationEquipement')
    def __str__(self):
        return f"Installation {self.id} pour {self.client.user.email}"

class InstallationEquipement(models.Model):
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

class SchemaInstallation(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, related_name='schema')
    fichier_schema = models.FileField(upload_to='schemas/', blank=True, null=True)
    # schema_json = models.JSONField(blank=True, null=True)

class Devis(models.Model):
    installation = models.OneToOneField(Installation, on_delete=models.CASCADE, related_name='devis')
    cout_achat = models.DecimalField(max_digits=12, decimal_places=2)
    cout_installation = models.DecimalField(max_digits=12, decimal_places=2)
    cout_maintenance = models.DecimalField(max_digits=12, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)

class ComparaisonEconomique(models.Model):
    devis = models.OneToOneField(Devis, on_delete=models.CASCADE, related_name='comparaison')
    cout_electricite_traditionnelle = models.DecimalField(max_digits=12, decimal_places=2)
    economies_potentielles = models.DecimalField(max_digits=12, decimal_places=2)
    duree_retour_investissement = models.PositiveIntegerField(help_text="Durée en années")
