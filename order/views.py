from django.shortcuts import render
from .form import OrderUploadForm


# Create your views here.
def order_upload_view(request):
    form = OrderUploadForm()
    return render(request,'order/order_upload.html',{'form': form})