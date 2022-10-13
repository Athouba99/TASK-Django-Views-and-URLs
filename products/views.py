from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1> Welcome </h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(
        f"""
        <h1> {product.name}</h1>
        <h2> {product.price}</h2>
        
        """,
    )
