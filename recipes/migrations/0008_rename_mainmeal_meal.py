# Generated by Django 3.2.15 on 2022-09-19 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20220919_1310'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MainMeal',
            new_name='Meal',
        ),
    ]
