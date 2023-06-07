from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def homee(request):
    return render(request,'play.html')


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail('Registratioon',"SUCCESSFULLY REGISTERED IN AHA",'gollavishnuyadav2@gmail.com',[NSUO.email],fail_silently=False)
            return HttpResponse('Regsitration is Susssessfulll')
        else:
            return HttpResponse('Not valid')
        
    return render(request,'registration.html',d)









def login_form(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Username and Password')
    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request,'movies.html')


def kid(request):
    return render(request,'kids.html')

def hanuman(request):
    return render(request,'hanuman.html')

@login_required
def display_profile(request):
    username=request.session.get('username')
    US=User.objects.get(username=username)
    PO=Profile.objects.get(username=US)
    d={'US':US,'PO':PO}
    return render(request,'profile.html',d)
def aha(request):
    return render(request,'aha.html')



def indian_idel(request):
    return render(request,'indian_idel.html')


def shows(request):
    return render(request,'shows.html')



def My_aha(request):
    return render(request,'My_aha.html')


def subscribe(request):
    return render(request,'subscribe.html')



@login_required

def change_password(request):
    if request.method=="POST":
        pw=request.POST['newPassword']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('PASSWORD CHANGED SUCCESSFULLY')
    return render(request,'change_password.html')




def reset_password(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('PASSWORD RESET PASSWORD')
        else:
            return HttpResponse ('INVALID CREDENTIALS')
    return render(request,'reset_password.html')