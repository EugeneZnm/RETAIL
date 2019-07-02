from decimal import Decimal
from django.conf import settings
from store.models import Item

# cart class allowing management of shopping cart
class Cart(object):


    def __init__(self, request):

        """
        initialisation of the cart with request object
        """
        # storage of current session making it accessible to other method of cart class
        self.session = request.session

        # getting cart from current session using self
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # saving an empty cart in the session if no cart is present. Product id used as keys in dictionary and quantity and price as value for each key to guarantee a product is not addded more than once in the cart
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1, update_quantity=False):

        """
        addition of a product to the cart and updating its quantity
        """    
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()           

    def save(self):
        # updating of the session cart
        self.session[settings.CART_SESSION_ID] = self.cart

        # marking the session as modified
        self.session.modified =True 