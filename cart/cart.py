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


    def add(self, item, quantity=1, update_quantity=False):

        """
        addition of a product to the cart and updating its quantity
        """    
        item_id = str(item_id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0, 'price': str(item.price)}
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()           

    def save(self):
        # updating of the session cart
        self.session[settings.CART_SESSION_ID] = self.cart

        # marking the session as modified session is changed and needs to be saved
        self.session.modified =True 

    def remove(self, item):
        """
        removing a product from the cart
        """    
        item_id = str(item.id)
        if item_id in self.cart:
            # removal of item from cart
            del self.cart[item_id]
            # save method to update the cart in session
            self.save()


