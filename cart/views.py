from .form import ProductCartForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
def product_upload_view(request):
    form = ProductCartForm()
    return render(request,"cart/product_get.html",{"form": form})

def add_to_cart(request):
    if request.method == 'POST':
        form = ProductCartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carts_list')
    else:
        form = ProductCartForm()
    return render(request, 'cart/add_to_cart.html', {'form': form})

def cart_list(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'cart_items': cart_items})