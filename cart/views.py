from django.shortcuts import render
from .form import CartUploadForm 
from django.shortcuts import redirect


# Create your views here.

def upload_cart(request):
    if request.method == 'POST':
        form = CartUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cart = Cart(image=request.FILES['image'])
            cart.save()
            return redirect('success_page')  
    else:
        form = CartUploadForm()
        return render(request, 'Cart/cart_upload.html', {'form': form})

def cart_list(request):
    carts = Cart.objects.all()
    return render (request, "cart/cart_list.html", {"carts":carts})


def cart_detail(request, id):
    cart = Cart.objects.get(id=id)
    return render(request, "cart/cart_detail.html", {"cart": cart})


def edit_cart_view(request,id):
   cart=Cart.objects.get(id=id)
   if request.method=='POST':
      form=CartUploadForm(request.POST,instance=Cart)
      if form.is_valid():
         form.save()
      return redirect("cart_edit_view",id=cart.id )

   else:
        form=CartUploadForm(instance=cart)
   return render (request,"cart/cart_detail.html",{"form":form})
     
     
