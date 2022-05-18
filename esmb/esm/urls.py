from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("club/",views.club,name='club'),
    path("actualités/",views.news,name='news'),
    path("actualités/<int:actualite_id>/",views.actualites,name='actualités'),
    path("inscription/",views.inscription,name="inscription"),
    path("talents/",views.talents,name="talents"),
    path("talents/groupes/<int:groupe_id>",views.groupe,name="groupe"),
    path("talents/coachs/<int:coach_id>",views.coach,name="coach"),
    path("talents/athletes/<int:athlete_id>",views.athlete,name="athlete"),
    path("galerie/",views.galerie,name="galerie"),
    path("credit/",views.credit,name="credit"),
]