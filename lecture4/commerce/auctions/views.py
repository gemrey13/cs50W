from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import *


def index(request):
    listing = AuctionListing.objects.all()
    return render(request, "auctions/index.html", {
        "auction_listing": listing
        })




def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))




def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def categories(request):
    pass



def watchlist(request, product_id):
    item_to_save = get_object_or_404(AuctionListing, pk=product_id)
    print(f'item to save : {item_to_save}')
    if Watchlist.objects.filter(user=request.user, auctionitem=product_id).exists():
        return HttpResponseRedirect(reverse("index"))

    user_list, create = Watchlist.objects.get_or_create(user=request.user)
    print(user_list)
    user_list.auctionitem.add(item_to_save)

    return render(request, "auctions/watchlist.html")


def watchlist_view(request):
    test = Watchlist.objects.filter(user=request.user)
    print(test)
    return render(request, 'auctions/watchlist.html', {
        "watchlist": Watchlist.objects.all().filter(user=request.user)
        })



def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        starting_bid = request.POST.get('starting_bid')
        select_category = Category.objects.get(name=request.POST.get('select_category'))
        image_url = request.FILES.get('image_url')

        print(f"title: {title}, description: {description}, price: {price}, starting_bid: {starting_bid}, category: {select_category}, image_url: {image_url}")
        q = AuctionListing(user=request.user, title=title, description=description, price=price, starting_bid=starting_bid, category=select_category, image_url=image_url)
        q.save()

        return HttpResponseRedirect(reverse('index'))


    return render(request, "auctions/create.html", {
        "categories": Category.objects.all()
        })


def listing(request, listingNo):
    get_listing_id = AuctionListing.objects.get(id=listingNo)
    user = request.user
    return render(request, "auctions/listing.html", {
        "listing": get_listing_id,
        "user": user
        })