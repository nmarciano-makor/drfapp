from django.db import models

class Usage(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=255)

class ConstructionElement(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    unite = models.CharField(max_length=100)
    impactUnitaireRechauffementClimatique = models.JSONField()
    dureeVieTypique = models.IntegerField()

class Zone(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    surface = models.FloatField()
    usage = models.IntegerField()
    constructionElements = models.JSONField()  # This should include [{id, quantite}]

class Batiment(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    surface = models.FloatField(null=True)
    zoneIds = models.JSONField()  # List of zone IDs
    usage = models.ForeignKey(Usage, on_delete=models.CASCADE,null=True)
    periodeDeReference = models.IntegerField()
