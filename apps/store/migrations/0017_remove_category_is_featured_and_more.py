# Generated by Django 5.0.2 on 2024-03-08 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_category_parent_remove_product_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_featured',
        ),
    ]
