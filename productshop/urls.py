"""productshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfproductshop/urls.py
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product
from django.contrib import admin
from django.urls import path
from products.views import get_home, get_products, get_product

from djreservation import urls as djreservation_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", get_home, name="home"),
    path("products/", get_products, name="product_list"),
    path("products/<int:product_id>/", get_product, name="product_detail"),
]

urlpatterns += djreservation_urls.urlpatterns
