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