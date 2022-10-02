from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request, "home.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)


def health(request):
    context = {}
    return render(request, "health.html", context)

def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes':recipes}
    return render(request, "recipes.html", context)

def cart(request):
    context = {}
    return render(request, "cart.html", context)

def checkout(request):
    context = {}
    return render(request, "checkout.html", context)

def breakfast(request):
    breakfast = Breakfast.objects.all()
    context = {'breakfast':breakfast}
    return render(request, "breakfast.html", context)

def chicken(request):
    chicken = Chicken.objects.all()
    context = {'chicken':chicken}
    return render(request, "chicken.html", context)

def meal(request):
    meal = Meal.objects.all()
    context = {'meal':meal}
    return render(request, "meal.html", context)

def meals(request):
    meals = Meals.objects.all()
    context = {'meals':meals}
    return render(request, "meals.html", context)

def bitings(request):
    bitings = Bitings.objects.all()
    context = {'bitings':bitings}
    return render(request, "bitings.html", context)

def starch(request):
    starch = Starch.objects.all()
    context = {'starch':starch}
    return render(request, "starch.html", context)

def vegan(request):
    vegan = Vegan.objects.all()
    context = {'vegan':vegan}
    return render(request, "vegan.html", context)

def bakery(request):
    bakery = Bakery.objects.all()
    context = {'bakery':bakery}
    return render(request, "bakery.html", context)

def lunch(request):
    lunch = Lunch.objects.all()
    context = {'lunch':lunch}
    return render(request, "lunch.html", context)

def dinner(request):
    dinner = Dinner.objects.all()
    context = {'dinner':dinner}
    return render(request, "dinner.html", context)

def meat(request):
    meat = Meat.objects.all()
    context = {'meat':meat}
    return render(request, "meat.html", context)

def fish(request):
    fish = Fish.objects.all()
    context = {'fish':fish}
    return render(request, "fish.html", context)

def single_recipe(request, id):
    single = Recipe.objects.get(id=id)
    # related_recipe = Recipe.objects.filter(category=single.category).exclude(id=id)[:5]
    context = {'single':single}
    return render(request, "single_recipe.html", context)


def single_starch(request, id):
    single = Starch.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_breakfast(request, id):
    single = Breakfast.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_bakery(request, id):
    single = Bakery.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)


def single_meals(request, id):
    single = Meals.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_bitings(request, id):
    single = Bitings.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)


def single_meat(request, id):
    single = Meat.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_fish(request, id):
    single = Fish.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_chicken(request, id):
    single = Chicken.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_meal(request, id):
    single = Meal.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def single_vegan(request, id):
    single = Vegan.objects.get(id=id)
    context = {'single':single}
    return render(request, "single_recipe.html", context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form. is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            
            try:
                send_mail(subject, message, 'derickchasimba@gmail.com', ['derickchasimba@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home")
    form = ContactForm()
    return render(request, "contact.html", {'form': form})


# def home(request):
#     about = About.objects.all()
#     context = {'about':about}
#     return render(request, "about.html", context)
