from django.shortcuts import render, get_object_or_404
from .models import Item, Category

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

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    # filter to get only available products
    prodcuts = Item.objects.filter(available=True)
    # filter products by a single category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render (request, 'shop.html', {'category': category, 'categories': categories, 'products': products})    

    