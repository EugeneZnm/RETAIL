from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug =  models.SlugField(max_length=200, db_index=True, unique=True)
    brand = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name ='category'
        verbose_name_plural = 'categories'

    def __str__ (self):
        return self.name    

# Create your models here.
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    discount_price = models.FloatField()
    discount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# specifying index for Id and SLug field together
    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        
    def __str__ (self):
        return self.title   