from django.db import models

# Create your models here.
class Product(models.Model):
        prod_name = models.CharField(max_length=100, blank=False, null=False)
        prod_price = models.IntegerField()
        prod_category = models.CharField(max_length=50)
        prod_quantity = models.IntegerField()
        prod_description = models.TextField()
        prod_image = models.ImageField(upload_to='products/')

        def __str__(self):
                return self.prod_name

class Author(models.Model):
        name = models.CharField(max_length=100, blank=False)

        def __str__(self):
                return self.name

class Book(models.Model):
        title = models.CharField(max_length=100, blank=False)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)

        def __str__(self):
                return self.title

class Library(models.Model):
        name = models.CharField(max_length=100, blank=False)
        book = models.ForeignKey(Book, on_delete=models.CASCADE)

        def __str__(self):
                return self.name
# make and run migrations after creating and registering the models
