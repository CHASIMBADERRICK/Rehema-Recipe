# Generated by Django 3.2.15 on 2022-09-15 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220914_1130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipe',
            new_name='Recipes',
        ),
    ]
