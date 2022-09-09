from django.urls import path
from .views import add_product, product_details, category_products, category_list, add_category

urlpatterns = [
    path("add", add_product, name="add_product"),
    path("<int:id>", product_details, name="product_details"),
    path("add_category", add_category, name="add_category"),
    path("category/<int:id>", category_products, name="category_products"),
    path("category_list", category_list, name="category_list")
]
