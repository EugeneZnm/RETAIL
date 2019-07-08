from .cart import Cart

def cart(request):
    # return of dictionary of objects available to all templates rendered using Request Context
    return {'cart': Cart(request)}

