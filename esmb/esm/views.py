from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import InscriptionForm, MessageForm
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Q

def index(request):
    date = timezone.now()
    periode_inscription = Periode_inscription.objects.all().first()
    actus = Actualite.objects.order_by('-id')[:6]
    nb_athletes = Athlete.objects.all().count()
    nb_coachs = Coach.objects.all().count()
    if not actus :
        actus_non_vide = False
    else:
        actus_non_vide = True
    for actu in actus:
        actu.text = actu.text[0:50:1]+" ..."
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid() :
            form.save()
            my_message = Message_contact.objects.last()

            email_body = "Email : "+str(my_message.email)+"\n"+"Nom : "+str(my_message.name)+"\n\n"+str(my_message.message)

            send_mail(
                my_message.subject,email_body,'esmbejaia@outlook.com',['esmbejaia@outlook.com'],fail_silently=False
            )
    context = {'actus':actus,'periode':periode_inscription, 'actus_non_vide':actus_non_vide, 'nb_athletes':nb_athletes,'nb_coachs':nb_coachs}
    return render(request,"esm/index.html",context)
def club(request):
    return render(request,"esm/club.html",{})
def news(request):
    actus = Actualite.objects.all()
    if not actus :
        actus_non_vide = False
    else:
        actus_non_vide = True
    for actu in actus:
        actu.text = actu.text[0:50:1]+" ..."
    context = {'actus':actus,'actus_non_vide':actus_non_vide}
    return render(request,"esm/news.html",context)
def actualites(request, actualite_id):
    actu = Actualite.objects.get(pk=actualite_id)
    if actu.type_event == "N" :
        actu.type_event = "Actualité"
    elif actu.type_event == "B":
        actu.type_event = "Blog"
    else :
        actu.type_event = "Competition"
    context = {'actu':actu}
    return render(request,"esm/new.html",context)
def inscription(request):
    athletes = Athlete.objects.all()
    emails = []
    for athlete in athletes :
        emails.append(athlete.email)
    periode = Periode_inscription.objects.first()
    maintenant = timezone.now()
    if (periode.debut <= maintenant and periode.fin >= maintenant):
        form = InscriptionForm()
        if request.method =='POST':
            form = InscriptionForm(request.POST,request.FILES)
            if form.is_valid() :
                if not request.POST.get('email') in emails :
                    form.save()
                    ath = Athlete()
                    ath.name=form.cleaned_data.get('name')
                    ath.first_name=form.cleaned_data.get('first_name')
                    ath.sexe=form.cleaned_data.get('sexe')
                    ath.email=form.cleaned_data.get('email')
                    ath.date_naissance=form.cleaned_data.get('date_naissance')
                    ath.image=form.cleaned_data.get('image')
                    ath.save()
                return redirect('..')
        context={'form':form}
        return render(request,"esm/inscriptions.html",context)
    else:
        pas_encore_message="Les Inscriptions Commencent Le "+str(periode.debut)+" Et Se Terminent Le "+str(periode.fin)
        context={'pas_encore_message':pas_encore_message}
        return render(request,"esm/inscriptions.html",context)

def talents(request):
    if request.method == "POST":
        search = request.POST['search']
        groupes= Groupe.objects.all().filter(name__contains=search)
        athletes = Athlete.objects.all().filter(Q(name__contains=search) | Q(first_name__contains=search),inscrit=True,afficher=True)
        coachs = Coach.objects.all().filter(Q(name__contains=search) | Q(first_name__contains=search))
        
    else:
        coachs = Coach.objects.order_by('id')
        athletes = Athlete.objects.order_by('id').filter(inscrit=True,afficher=True)
        groupes = Groupe.objects.order_by('id')

    for coach in coachs :
        coach.description = coach.description[0:90:1]+" ..."
    for athlete in athletes:
        if athlete.description:
            athlete.description = athlete.description[0:50:1]+" ..."

    context={'coachs':coachs,'athletes':athletes,'groupes':groupes}
    return render(request,"esm/talents.html",context)

def groupe(request,groupe_id):
    groupe = Groupe.objects.get(pk=groupe_id)
    athletes = Athlete.objects.filter(groupe=groupe)
    context = {'groupe':groupe, 'athletes':athletes}
    return render(request,"esm/groupe.html",context)

def coach(request,coach_id):
    coach = Coach.objects.get(pk=coach_id)
    groups = Groupe.objects.filter(coach=coach)
    context={'talent':coach, 'groups':groups, 'talent_category':'Coach'}
    return render(request,"esm/talent-details.html",context)
def athlete(request,athlete_id):
    athlete = Athlete.objects.get(pk=athlete_id)
    context={'talent':athlete,'talent_category':'Athlete'}
    return render(request,"esm/talent-details.html",context)
def galerie(request):
    photos = Gallery_photo.objects.all()
    context={'photos':photos}
    return render(request,"esm/galery.html",context)

# Create your views here.