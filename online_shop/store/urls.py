from . import views
from django.urls import path


urlpatterns = [
    path('', views.store, name='products'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
]