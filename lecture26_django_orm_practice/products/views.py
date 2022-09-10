from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponseNotFound


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add.html")
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def update_product(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        if product.user == request.user:
            if request.method == "GET":
                return render(request, "products/update.html", {"product": product})
            else:
                product.title = request.POST.get("title")
                product.description = request.POST.get("description")
                product.user = request.user
                product.save()
                return redirect("/")
        else:
            return HttpResponseNotFound("Forbidden")
    else:
        return redirect("/")
