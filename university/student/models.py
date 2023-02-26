from django.db import models

class Matiere(models.Model):
    libelle= models.CharField(max_length=20)
    note_ds = models.FloatField()
    note_ex = models.FloatField()
    def __str__(self):
        return self.libelle
    def moy(self):
        return self.note_ds * 0.4 + self.note_ex * 0.6
    


class Classes (models.Model):
    libelle = models.CharField(max_length=20)
    matiere= models.ManyToManyField(Matiere)
    def __str__(self):
        return self.libelle
    
class Etudiant (models.Model):
    nom = models.CharField(max_length=20)
    prenom= models.CharField(max_length=20)
    age = models.IntegerField()
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
    
