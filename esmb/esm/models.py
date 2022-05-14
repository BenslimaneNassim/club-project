from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
SEXES = (
    ('M','Homme'),
    ('F','Femme')
)
CATEGORIES = (
    ('P','Poussin'),
    ('E','Ecole'),
    ('B','Benjamin'),
    ('M','Minime'),
    ('C','Cadets'),
    ('J','Junior'),
    ('S','Senior'),
)
TYPES = [
    ('C','Competition'),
    ('B','Blog'),
    ('N','Actualités'),
]
class Human(models.Model):
        name = models.CharField(max_length=25)
        first_name = models.CharField(max_length=25)
        date_naissance = models.DateField()
        email = models.EmailField(max_length=200,null=True,blank=True)
        image = models.ImageField(null=True, blank=True, upload_to="profilephoto/")
        description = models.TextField(null=True,blank=True)
        sexe = models.CharField(choices = SEXES, max_length=1)
        def __str__(self):
            return self.name +' '+ self.first_name
        class Meta:
            abstract = True

class Coach(Human):
    pass

class Groupe(models.Model):
    name = models.CharField(max_length=10)
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
    sexe = models.CharField(choices = SEXES, max_length=1)
    emploi = models.ImageField(null=True, blank=True, upload_to="emplois-du-temps/")
    category = models.CharField(choices = CATEGORIES, max_length=1)
    def __str__(self):
            return self.name


class Athlete(Human):
    groupe = models.ForeignKey(Groupe, on_delete=models.PROTECT,null=True,blank=True)
    inscrit = models.BooleanField(default=False)
    afficher = models.BooleanField(default=False)

class Actualite(models.Model):
    title = models.CharField(max_length=100, null = False,blank=False)
    text = models.TextField(max_length=10000, null=True,blank=True)
    image = models.ImageField(null=True,blank=True, upload_to="actualités/")
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    type_event = models.CharField(choices = TYPES, max_length=1, default='N')
    def __str__(self):
            return self.title

class Gallery_photo(models.Model):
    title = models.CharField(max_length=20,null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)
    display = models.BooleanField(default = False)
    image = models.ImageField(blank=False,null=False, upload_to="galerie/")
    def __str__(self):
            return str(self.id)
            
class Inscription(models.Model):
    #athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE)
    #accepted = models.BooleanField(default=False)
    name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    date_naissance = models.DateField()
    email = models.EmailField(max_length=200,null=True,blank=True)
    sexe = models.CharField(choices = SEXES, max_length=1)
    phone = PhoneNumberField()
    image = models.ImageField(blank=True,null=True,upload_to="inscriptions/photos/")
    scan_1 = models.ImageField(blank=False,null=False,upload_to="inscriptions/extrait-naissance/")
    scan_2 = models.ImageField(blank=False,null=False,upload_to="inscriptions/scans-2/")
    scan_3 = models.ImageField(blank=True,null=True,upload_to="inscriptions/scans-3/")
    def __str__(self):
        return self.name+" "+self.first_name

class Periode_inscription(models.Model):
    debut = models.DateTimeField(null=False, blank=False)
    fin = models.DateTimeField(null=False, blank=False)
    def save(self, *args, **kwargs):
        if not self.pk and Periode_inscription.objects.exists():
            raise ValidationError("Il ne peut y avoir qu'ne seule periode d'inscription à la fois. ")
        return super(Periode_inscription, self).save(*args, **kwargs)
class Message_contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message= models.TextField(max_length=10000)

