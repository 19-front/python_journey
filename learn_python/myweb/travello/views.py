from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    #destination 1
    dest1 = Destination()
    dest1.name = "Accra"
    dest1.desc = "The City that Never Sleep"
    dest1.img = "destination_1.jpg"
    dest1.prices = 700
    
    #destination 2
    dest2 = Destination()
    dest2.name = "Takoradi"
    dest2.desc = "The City of Wonders"
    dest2.img = "destination_2.jpg"
    dest2.prices = 610
    
    #destination 3
    dest3 = Destination()
    dest3.name = "Kumasi"
    dest3.desc = "The Garden City"
    dest3.img = "destination_3.jpg"
    dest3.prices = 770
    
    dests = [dest1, dest2, dest3]
    
    return render (request, "index.html", {"dests": dests})
