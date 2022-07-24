from django import urls
from django.urls import URLPattern, path
from product import views


urlpatterns = [
    path("",views.book),
    
]