from django.urls import path
from GroceryApp.views import *

app_name = "GroceryApp"

urlpatterns = [
    path("", index, name = "Home"),
    path("checkout", checkout, name= "checkout"),
    path("contact", contact, name= "contact"),
    path("shop_details/<str:title>/", shop_details, name= "shop_details"),
    path("shop_grid/", shop_grid, name= "shop_grid"),
    path("shopping_cart",shopping_cart, name= "shopping_cart"),
    path("shop_grid/<str:category>/", shop_grid, name="shop_grid"),
    path("wish_list", wish_list, name= "wish_list"),
    path("shop_grid/<str:product>/", shop_grid, name="shop_grid_search"),
    ]