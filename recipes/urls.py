from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("recipes/", views.recipes, name="recipes"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("breakfast/", views.breakfast, name="breakfast"),
    path("meal/", views.meal, name="meal"),
    path("bitings/", views.bitings, name="bitings"),
    path("starch/", views.starch, name="starch"),
    path("vegan/", views.vegan, name="vegan"),
    path("bakery/", views.bakery, name="bakery"),
    path("lunch/", views.lunch, name="lunch"),
    path("dinner/", views.dinner, name="dinner"),
    path("meals/", views.meals, name="meals"),
    path("meat/", views.meat, name="meat"),
    path("fish/", views.fish, name="fish"),
    path("chicken/", views.chicken, name="chicken"),
    path("health/", views.health, name="health"),
    path("single_recipe/<int:id>/", views.single_recipe, name="single_recipe"),
    path("contact/", views.contact, name="contact"),
    path("single_starch/<int:id>/", views.single_starch, name="single_starch"),
    path("single_breakfast/<int:id>/", views.single_breakfast, name="single_breakfast"),
    path("single_bakery/<int:id>/", views.single_bakery, name="single_bakery"),
    path("single_meals/<int:id>/", views.single_meals, name="single_meals"),
    path("single_bitings/<int:id>/", views.single_bitings, name="single_bitings"),
    path("single_fish/<int:id>/", views.single_fish, name="single_fish"),
    path("single_meat/<int:id>/", views.single_meat, name="single_meat"),
    path("single_meal/<int:id>/", views.single_meal, name="single_meal"),
    path("single_vegan/<int:id>/", views.single_vegan, name="single_vegan"),
    path("single_chicken/<int:id>/", views.single_chicken,name="single_chicken"),
]