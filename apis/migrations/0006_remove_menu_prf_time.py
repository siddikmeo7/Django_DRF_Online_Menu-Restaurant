# Generated by Django 5.0 on 2024-11-21 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_rename_time_category_menu_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='prf_time',
        ),
    ]
