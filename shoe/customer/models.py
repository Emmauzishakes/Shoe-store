from django.db import models

# Create your models here.

SHOE_BRANDS = (
    ('DD', 'Adidas'),
    ('BA', 'Bata'),
    ('CO', 'Converse'),
    ('FI', 'Fila'),
    ('NB', 'New Balance'),
    ('NI', 'Nike'),
    ('PU', 'Puma'),
    ('RB', 'Reebok'),
    ('TL', 'Timberland'),
    ('VA', 'Vans'),
)

class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=SHOE_BRANDS, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ("id",)
    
class ProductNew(models.Model):
    title = models.ForeignKey(Product, related_name="productnew", on_delete=models.CASCADE)
    discounted_price = models.FloatField(default="5")
    product_image = models.ImageField(upload_to='product', default="product.png")

    class Meta:
        ordering = ("-discounted_price",)
        verbose_name = ("New Products")
        verbose_name_plural = ("New Products")

    def __str__(self):
        return self.title.title
    