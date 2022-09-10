from django.urls import path
from .views import add_product, product_details, update_product

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/update/<int:id>", update_product, name="update_product"),
]