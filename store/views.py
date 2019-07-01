from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.
def home(request):
     
    return render(request, "index.html")

def products(request):
    context = {
        'items': Item.objects.all()
    }    
    return render (request, "shop.html", context)


def product(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }    
    return render (request, "product.html", context)