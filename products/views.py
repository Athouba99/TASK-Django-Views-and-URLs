# for the views and URLs task
from multiprocessing import context
from pipes import Template
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# for templates task
from django.shortcuts import render
from django.template import Context
from django.template import Template

# Create your views here.
def get_home(request):
    return HttpResponse(f"<h1> Welcome </h1>")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": {
            "name": product.name,
            "description": product.description,
            "price": product.price,
        }
    }
    return render(
        request,
        "product-detail.html",
    )  # render means to show
    # return HttpResponse( [only for V&R task no need for it for template ]
    #     f"""
    #      <h1> {product.name}</h1>
    #      <h2> {product.price}</h2>
    #      """,
    # )


def get_products(request, product_id):  # template task
    ...


def render_context_with_context(html_data, context_data):
    template = Template(html_data)
    context = Context(context_data)
    return template.render(context)
