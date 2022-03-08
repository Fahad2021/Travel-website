from django.shortcuts import render,HttpResponse
import datetime
from .models import*
from django.core.mail import send_mail


def home(request):
    return render(request,"home.html")
    
def package(request):
    package=Package.objects.all()
    context = {'packages':package}
    # print(context)
    return render(request,"package.html",context)

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        data={
            'name':name,
            'email':email,
            'phone':phone,
            'message':message
        }
        messages = '''
        New Message: {}
        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['phone'],message,'',['fahadrahman810@gmail.com'])
        

    return render(request,"contact.html",{})

def about(request):
    hotel=Hotel.objects.all()
    context={'hotel':hotel}
    # print(context)
    return render(request,"about.html",context)

def condition(request):
    return render(request,"condition.html")

def viewPhoto(requespt,k):
    photo=Photo.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})

def login(request):
    return render(request,"login-reg.html")

def register(request):
    return render(request,"register.html")
