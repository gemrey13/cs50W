from django.urls import path

from . import views

"""
 When the form is submitted. It will submit here in the url with the name search
 The search path will get the q in form using the function in views.search
 The path for seach cannot be empty because it need a url to display the output
"""
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.search, name="search"),
    path("wiki/<str:title>", views.entry, name="entry"),
]


