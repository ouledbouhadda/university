from django.contrib import admin

from .models import Etudiant,Classes,Matiere
admin.site.register(Etudiant)
admin.site.register(Classes)
admin.site.register(Matiere)