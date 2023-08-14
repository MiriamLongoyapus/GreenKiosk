from django.shortcuts import render
from .form import DeliveryUploadForm
# from .models import Delivery

# Create your views here.
def delivery_upload_view(request):
    form = DeliveryUploadForm()
    return render(request,'delivery/delivery_upload.html',{'form': form})

# def edit_delivery_view(request, id):
#     delivery = get_object_or_404(Delivery, id=id)
    
#     if request.method == 'POST':
#         form = DeliveryEditForm(request.POST, instance=delivery)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery_details_view', id=id)  # Redirect to delivery details page
#     else:
#         form = DeliveryEditForm(instance=delivery)
    
#     return render(request, 'edit_delivery.html', {'form': form, 'delivery': delivery})
