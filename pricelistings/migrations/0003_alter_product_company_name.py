# Generated by Django 5.0.2 on 2024-03-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricelistings', '0002_product_company_name_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
    ]