from django.db import models

# Create your models here.
from django.db import models
from installation.models import Installation

class Incident(models.Model):
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE, related_name='incidents')
    description = models.TextField()
    date_signalisation = models.DateTimeField(auto_now_add=True)

class Maintenance(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='maintenances')
    solution_proposee = models.TextField()
    cout_estime = models.DecimalField(max_digits=12, decimal_places=2)
    temps_estime_heure = models.PositiveIntegerField()
    date_intervention = models.DateTimeField(blank=True, null=True)

class QuestionMaintenance(models.Model):
    texte_question = models.TextField()

class ReponseMaintenance(models.Model):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='reponses')
    question = models.ForeignKey(QuestionMaintenance, on_delete=models.CASCADE)
    reponse = models.TextField()
