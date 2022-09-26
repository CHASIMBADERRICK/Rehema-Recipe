# Generated by Django 3.2.15 on 2022-09-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatriesandBakery',
            new_name='Bakery',
        ),
        migrations.AlterField(
            model_name='breakfast',
            name='Image',
            field=models.ImageField(upload_to='recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Image',
            field=models.ImageField(upload_to='recipe'),
        ),
    ]
