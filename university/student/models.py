from django.db import models


class Classes (models.Model):
    libelle = models.CharField(max_length=20)

    
class Etudiant (models.Model):
    nom = models.CharField(max_length=20)
    prenom= models.CharField(max_length=20)
    age = models.IntegerField()
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
