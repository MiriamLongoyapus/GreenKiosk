from django.shortcuts import render
from .form import CartUploadForm

def cart_upload_view(request):
    form = CartUploadForm()
    return render(request,"cart/cart_upload.html",{"form": form})
