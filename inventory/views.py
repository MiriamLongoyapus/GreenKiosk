from django.shortcuts import render

# Create your views here.
from .forms import ProductUploadForm
# from django.shortcuts import render

def product_upload(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form})