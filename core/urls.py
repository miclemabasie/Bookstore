from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ContactUsView,
    ProductDetailView,
    ProductListView,

)


app_name = 'core'


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('products/<slug:tag>/', ProductListView.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]
