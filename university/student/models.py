from django.db import models

class Matiere(models.Model):
    libelle= models.CharField(max_length=20)
    note_ds = models.FloatField()
    note_ex = models.FloatField()


class Classes (models.Model):
    libelle = models.CharField(max_length=20)
    matiere= models.ManyToManyField(Matiere)

    
class Etudiant (models.Model):
    nom = models.CharField(max_length=20)
    prenom= models.CharField(max_length=20)
    age = models.IntegerField()
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
