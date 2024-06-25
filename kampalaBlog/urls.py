from django.urls import path
from . import views



urlpatterns =  [
    path('', views.index ,name='index'),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('products1/',views.products1, name='products1'),
    path('products2/',views.products2, name='products2'),
    path('products3/',views.products3, name='products3'),
    path('products4/',views.products4, name='products4'),
    path('products5/',views.products5, name='product5'),
    path('single_product/',views.single_product, name='single_product'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
]