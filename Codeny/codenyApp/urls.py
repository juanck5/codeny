
from django.conf.urls import url, include

# vistas a usar.
from codenyApp.views import index

urlpatterns = [
    url(r'^$', index),
    
]