from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
    path('products', views.product_list, name='products'),
    path('product/<int:pk>', views.product, name='product'), # pk == primary key
    path('register', views.register,name='register'),
] 

# now I can create a json file like this: localhost/products.json
urlpatterns = format_suffix_patterns(urlpatterns)