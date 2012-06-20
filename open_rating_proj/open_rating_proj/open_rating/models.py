from django.db import models

class Reglage(models.Model):
    historique=models.IntegerField()
    exposition=models.IntegerField()
    macro=models.IntegerField()
    social=models.IntegerField()
    
# Create your models here.
class Pays(models.Model):
    weo=models.IntegerField()
    nom=models.CharField(max_length=50)
#comportement de paiement
    defaut_exterieur=models.BooleanField()
    defaut_interieur=models.BooleanField()
    defaut_50=models.BooleanField()

    hdi=models.FloatField()
    chomage=models.FloatField()
    revenus=models.IntegerField()
    
    credibilite=models.IntegerField()
    stabilite=models.IntegerField()
    conflit=models.IntegerField()
    
    dette_PIB=models.IntegerField()
    deficit_PIB=models.FloatField()
    deficit_2012=models.FloatField()
    deficit_2013=models.FloatField()
    deficit_2014=models.FloatField()
    deficit_2015=models.FloatField()
    deficit_2016=models.FloatField()

    croissance=models.FloatField()
    croissance_2012=models.FloatField()
    croissance_2013=models.FloatField()
    croissance_2014=models.FloatField()
    croissance_2015=models.FloatField()
    croissance_2016=models.FloatField()

    inflation=models.FloatField()
    bop=models.FloatField()

    maturite=models.FloatField()
    interet=models.FloatField()
    etranger=models.FloatField()
    devise=models.FloatField()
