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

    def __iter__(self):
        """
        Retrieving product instances in the cart by iterating over the items in the cart and getting products from the database
        """        
        item_ids = self.cart.keys()

        # getting product objects and adding them to the cart
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            self.cart[str(item.id)]['item'] = item
        # iterating over the cart items and convert the item prices back to the decimal adding a total price attribute to each item
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item    

    def __len__(self):
        """
        counting and return all the items in the cart
        """
        
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):

        # sum of items in cart returned
        return sum(Decimal(item['price']) * item ['quantity'] for item in 
    self.cart.values())

    def clear(self):
        # removing cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True