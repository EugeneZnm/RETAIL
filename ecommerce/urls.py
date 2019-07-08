from django.conf import settings
from django.contrib import admin
from django.urls import path, include

app_name = "cart"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace ='cart')),
    path('', include('store.urls', namespace='store')),
    
]
