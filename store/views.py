from django.shortcuts import render, get_object_or_404
from .models import Item, Category
from cart.forms import CartAddItemForm

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

# Retrieving all available products by availability and Category
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    # filter to get only available products
    items = Item.objects.filter(available=True)
    # filter products by a single category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    return render (request, 'shop.html', {'category': category, 'categories': categories, 'items': items})    

# Retrieving a single product
def product_detail(request, id ,slug):
    item = get_object_or_404(Item, id=id, slug=slug,available=True)

    cart_product_form = CartAddItemForm()
    return render(request, 'product.html', {'item': item, 'cart_product_form': cart_product_form})    
