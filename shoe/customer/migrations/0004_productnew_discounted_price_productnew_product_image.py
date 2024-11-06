# Generated by Django 5.0.6 on 2024-11-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_productnew_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='productnew',
            name='discounted_price',
            field=models.FloatField(default='5'),
        ),
        migrations.AddField(
            model_name='productnew',
            name='product_image',
            field=models.ImageField(default='product.png', upload_to='product'),
        ),
    ]