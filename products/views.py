from django.shortcuts import render, redirect
from rest_framework import viewsets

# import models
from . models import Product

# import serializers
from . serializers import ProductSerializer

# Create your views here.
class ProductView(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer



def home(request):
        return render(request, 'home.html')

def insert(request):
        return render(request, 'insert.html')

def insert_data(request):
        # Capture user input
        if request.method == "POST":
                prod_name = request.POST['prod_name']
                prod_price = request.POST['prod_price']
                prod_category = request.POST['prod_category']
                prod_quantity = request.POST['prod_quantity']
                prod_description = request.POST['prod_description']
                prod_image = request.FILES['prod_image']

                # Save user input to the database
                product = Product(
                        prod_name=prod_name,
                        prod_price=prod_price,
                        prod_category=prod_category,
                        prod_quantity=prod_quantity,
                        prod_description=prod_description,
                        prod_image=prod_image
                )
                product.save()
                return redirect('products:home')
        return render(request, 'insert.html')

def view_products(request):
        products = Product.objects.all()
        return render(request, 'view_products.html', {'products': products})

# Function to retrieve one item
def view_product(request, id):
        product = Product.objects.get(id=id)
        return render(request, 'products.html', {'product': product})

# Function to update product details
def update_product(request, id):
        product = Product.objects.get(id=id)
        # Getting the new product values
        if request.method == "POST":
                prod_name = request.POST['prod_name']
                prod_price = request.POST['prod_price']
                prod_category = request.POST['prod_category']
                prod_quantity = request.POST['prod_quantity']
                prod_description = request.POST['prod_description']
                prod_image = request.FILES['prod_image']

                # Equating the new values to the existing product values
                product.prod_name = prod_name
                product.prod_price = prod_price
                product.prod_category = prod_category
                product.prod_quantity = prod_quantity
                product.prod_description = prod_description
                product.prod_image = prod_image

                # Save the new values to the database
                product.save()

                # Redirect to the view_products page
                return redirect('products:view_products')

        return render(request, 'update_product.html', {'product': product})

def delete_product(request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('products:view_products')