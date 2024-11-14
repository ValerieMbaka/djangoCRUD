from django.shortcuts import render, redirect

# import models
from products.models import Product

# Create your views here.
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