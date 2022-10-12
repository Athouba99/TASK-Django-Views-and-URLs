from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1> Welcome </h1>")


def get_product(request, product_id):
    product = product.object.get(id=product_id)
    return HttpResponse(product)
