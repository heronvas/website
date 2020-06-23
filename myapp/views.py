from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    return render(request, 'myapp/home.html')
def home(request):
    if(request.method == 'POST'):
        message = request.POST['message']
        message_name = request.POST['message-name']    
        message_email = request.POST['message-email']
        send_mail(message_name,
                  message,
                  message_email,
                  [settings.EMAIL_HOST_USER],
                  fail_silently=False)

        return render(request, 'myapp/basic.html', {'message_name': message_name})

    else:
        return render(request, 'myapp/basic.html')

def about(request):
    return render(request, 'myapp/about.html')


# Create your views here.
