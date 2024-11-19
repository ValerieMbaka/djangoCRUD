from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
        path('', views.home, name='home'),
        path('insert/', views.insert, name='insert'),
        path('insert_data/', views.insert_data, name='insert_data'),
        path('view_products/', views.view_products, name='view_products'),
        path('product/<id>/', views.view_product, name='product'),
        path('update/<id>/', views.update_product, name='update'),
        path('delete/<id>/', views.delete_product, name='delete'),
        path('search/', views.search, name='search'),
]