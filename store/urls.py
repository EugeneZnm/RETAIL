from django.urls import path, include
from django.conf.urls import url
from .import views

app_name = 'store'
urlpatterns = [
   path('', views.home, name='home'), 
   path('shop/', views.product_list, name='product_list'),

    #  path providing a category_slug parameter to the view for filtering products by a given category
   url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    #  path passing Id and slug parameter to view in order to retrieve a specific product
   url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),

#    path('<int:item_id>', views.product, name='product')
]