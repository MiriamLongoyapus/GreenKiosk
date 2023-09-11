from django.shortcuts import render
from .form import DeliveryUploadForm


# Create your views here.
def delivery_upload_view(request):
    form = DeliveryUploadForm()
    return render(request,'delivery/delivery_upload.html',{'form': form})

