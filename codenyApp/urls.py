
from django.conf.urls import url, include

# Views use.
from codenyApp.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^administracion$', boardAdmin , name="boardAdmin"),

    #REQUESTS
    url(r'^contactForm/$', contactForm , name= 'contactForm'),
    
]