
from django.conf.urls import url, include

# Views use.
from codenyApp.views import *

urlpatterns = [
    url(r'^$', index , name="index"),
    url(r'^administracion$', boardAdmin , name="boardAdmin"),
    url(r'^login$',login, name="login" ),
    url(r'^tables$',tables, name="tables" ),
    url(r'^contactForm/$', contactForm , name= 'contactForm'),
    url(r'^profile$',profile, name="profile" ),
    url(r'^billing$',billing, name="billing" ),
     url(r'^funcion/$', funcion , name= 'funcion'),
    #REQUESTS
    url(r'^loginAccess/$', login_user , name= 'loginAccess'),
]