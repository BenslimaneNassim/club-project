from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Athlete)
admin.site.register(Coach)
admin.site.register(Groupe)
admin.site.register(Actualite)
admin.site.register(Gallery_photo)
admin.site.register(Inscription)
admin.site.register(Periode_inscription)
admin.site.register(Message_contact)