from .models import Product
from django.shortcuts import render
from .forms import ProductUploadForm
# from .forms import products_list

# from django.shortcuts import render

def product_upload(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form}),

def products_list(request):
    product=Product.objects.all()
    return render(request, "inventory/products_list.html",{"product": product})
  

def product_detail_view(request, id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_details.html",{"product": product})
