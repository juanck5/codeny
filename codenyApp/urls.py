
from django.conf.urls import url, include

# Views use.
from codenyApp.views import *

urlpatterns = [
    url(r'^$', index),


    #REQUESTS
    url(r'^contactForm/$', contactForm , name= 'contactForm'),
    
]