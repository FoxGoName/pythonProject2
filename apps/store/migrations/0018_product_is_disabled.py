# Generated by Django 5.0.2 on 2024-03-17 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_category_is_featured_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
    ]
