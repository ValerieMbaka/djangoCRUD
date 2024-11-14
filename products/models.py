from django.db import models

# Create your models here.
class Product(models.Model):
        prod_name = models.CharField(max_length=100, blank=False, null=False)
        prod_price = models.IntegerField()
        prod_category = models.CharField(max_length=50)
        prod_quantity = models.IntegerField()
        prod_description = models.TextField()
        prod_image = models.ImageField(upload_to='products/')

