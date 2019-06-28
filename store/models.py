from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('LC','Laptops & Computers'),
    ('ST','Smartphones & Tablets'),
    ('G','Gadgets'),
    ('A','Accessories')
)

LABEL_CHOICES = (
    ('P','Primary'),
    ('S','Secondary'),
    ('D','danger'),
)

BRAND_CHOICES = (
    ('A', 'Apple'),
    ('G', 'Google'),
    ('X', 'Xiaomi'),
    ('SG', 'Samsung'),
    ('N', 'Nokia'),
    ('O+', 'OnePlus'),
    ('Op', 'Oppo'),
    ('BB', 'Blackberry'),
    ('SY', 'Sony'),
    ('H', 'Huawei'),
)

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    brand = models.CharField(choices=BRAND_CHOICES,max_length=20)
    label = models.CharField(choices=LABEL_CHOICES, max_length=100)
    discount = models.IntegerField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# product added to cart
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    # date of addition
    start_date = models.DateTimeField(auto_now_add=True)

    # date order was made
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.title
