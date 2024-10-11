from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # La ruta vacía hace que esta sea la página principal
]
