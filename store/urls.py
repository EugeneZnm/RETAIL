from django.urls import path, include
from .import views

app_name = 'store'
urlpatterns = [
   path('', views.home, name='home'), 
   path('shop/', views.products, name='products'),
   path('<int:item_id>', views.product, name='product')
]