from inventory.models import Product
from django.shortcuts import render
from .forms import ProductUploadForm

# from django.shortcuts import render

def product_upload(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form}),

def product_list(request):
    product=Product.objects.all()
    return render(request, "inventory/product_list.html",{"product": product})
  
def product_detail_view(request, id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_details.html",{"product": product})

# def product_update_view(request, id):
#   product=Product.objects.get(id=id)
#   return render(request, "inventory/edit_product.html", {"form": product})

def product_update_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
         form = ProductUploadForm(request.POST, instance=product)
         if form.is_valid():
            form.save()
            return redirect("product_detail", id=product.id)
    else:
            form = ProductUploadForm(instance=product)
            return render(request, "inventory/edit_product.html", {'form': form})


# def product_update_view(request, id):
#     product=Product.objects.get(id=id)

#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             # You might want to redirect or render a success message here
#     else:
#         form = Product(instance=product)
    
    # return render(request, "inventory/edit_product.html", {"product": product})