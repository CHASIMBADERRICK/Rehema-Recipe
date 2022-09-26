from django.db import models

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to="recipe")
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    
class Breakfast(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to="recipe")
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()


class Meals(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()


class Bitings(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()


class Starch(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    

class Vegan(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    

class Bakery(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    
class Meat(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    
    
class Fish(models.Model):
    Title = models.CharField(max_length=255)
    Image = models.ImageField(max_length=2083)
    Description = models.TextField()
    Instructions = models.TextField()
    Ingredients = models.TextField()
    PrepTime = models.CharField(max_length=5)
    CookTime = models.CharField(max_length=5)
    Servings = models.CharField(max_length=5)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    
    
class About(models.Model):
    Image = models.ImageField(max_length=2083)
    

