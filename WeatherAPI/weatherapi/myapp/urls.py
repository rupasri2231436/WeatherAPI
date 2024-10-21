from django.urls import path
from .views import home, weatherinfo, contactmail
urlpatterns = [
    path('', home, name='home'),
    path('weatherinfo',weatherinfo,name='weatherinfo'),
    path('contactmail',contactmail,name='contactmail')
]