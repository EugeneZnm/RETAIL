from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    # url(r'^cart/(?P<item_id>\d+)/$', views.cart_add, name='cart_add'),
    path('cart/<int:item_id>/', views.cart_add, name='cart_add'),    
    url(r'^remove/(?P<item_id>\d+)/$', views.cart_remove, name='cart_remove')    
]