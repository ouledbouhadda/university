from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emploi',views.emploi,name='emploi' ),
    path('test',views.test,name='test')
]