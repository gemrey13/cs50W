from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("goku/", views.goku, name="goku"),
    path("<str:name>", views.name, name="Boom"),
    path("greet/<str:name>", views.greet, name="Name")
]