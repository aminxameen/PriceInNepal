from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField(null=True, default=timezone.now)

    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.name
