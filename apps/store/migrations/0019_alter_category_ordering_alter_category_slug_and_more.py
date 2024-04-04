# Generated by Django 5.0.2 on 2024-04-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_product_is_disabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='ordering',
            field=models.IntegerField(default=0, verbose_name='Ordering'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_visit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Visit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='num_available',
            field=models.IntegerField(default=1, verbose_name='Number Available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='num_visits',
            field=models.IntegerField(default=0, verbose_name='Number of Visits'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
