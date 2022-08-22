from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from . models import *

# Create your views here.

def index(request):
    obj = Project.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data={
            'name': name,
            'email': email,
            'message': message
        }
        message = '''
        new message :{}
        
        from : {}
        '''.format(data['message'],data['email'])
        send_mail(data['name'],message,'',['emailtestgin@gmail.com'])
    return render(request, 'home.html',{'pro':obj})

# def project()


def aboutme(request):
    return render(request, 'about.html')
