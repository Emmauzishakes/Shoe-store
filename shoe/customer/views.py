from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductNew, Cart
from django.views import View
from django.db.models import Count
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    product = Product.objects.all()
    productNew = ProductNew.objects.all()[:4]
    return render(request, 'customer/home.html', {
         'product': product,
         'productNew': productNew,    
    })

def about(request):
    return render(request, 'customer/about.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, 'customer/category.html', locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "customer/category.html", locals())
    
class ProductDetail(View):
    def get(self, request, pk):
            product = Product.objects.get(pk=pk)
            return render(request, "customer/productdetail.html", locals())

class CartDetail(View):
     def get(self, request):
        product = Product.objects.all()
        productNew = ProductNew.objects.all()[:8]
        cart = Cart.objects.all()
          
        return render(request, "customer/cartdetail.html", locals())