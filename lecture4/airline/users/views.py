from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))



def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

	return render(request, "users/login.html", {})




def logout_view(request):
	pass