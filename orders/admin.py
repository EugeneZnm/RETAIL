from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    """
    model included inline in admin dashboard, allowing it to appear in the same edit page as the parent model
    """
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inline = [OrderItemInline] 

admin.site.register(Order, OrderAdmin)       