from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category

from multiprocessing import context


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            categories = Category.objects.all()
            return render(request, "products/add.html", {"categories": categories})
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.categories = request.POST.get("categories")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def add_category(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add_category.html")
        else:
            category = Category()
            category.category_title = request.POST.get("category_title")
            category.user = request.user
            category.save()
            return redirect("/")
    else:
        return redirect("/")


def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"categories": categories})


def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return render(request, "products/category_products.html", {"category": category, "products": products})
