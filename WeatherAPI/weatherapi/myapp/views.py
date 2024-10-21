from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Contact
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,"home.html")


def weatherinfo(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '3c33807ee29cab406b4307d7274659dd'
        url =  f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})
    return render(request,"weatherappinput.html")


def contactmail(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        comment = request.POST['comment']
        email = request.POST['email']
        subject = "If you have any query regarding TTMS"
        comment1 = comment + " This is System generated mail. So donot respond to this mail"

        data = Contact(firstname=firstname,lastname=lastname,comment=comment,email=email)
        data.save()
        send_mail(
            subject,
            comment1,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently= False
        )
        return HttpResponse("<h1 align=center>Mail Sent Successfully</h1>")
    return render(request,"Contact.html")
