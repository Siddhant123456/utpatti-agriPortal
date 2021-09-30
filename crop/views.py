import crop
from django.http.response import HttpResponse
from account.models import FarmerProfile
from django.contrib import messages
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .models import Crop
# Create your views here.


def store(request):
    return render(request,'store.html')


def upload_crop(request):
    if request.method == 'POST':
        crop_name = request.POST['crop_name']
        image = request.FILES['img']
        description = request.POST['description']
        base_price = request.POST['base_price']
        stock = request.POST['stock']
        user = request.user

        if user.profile == 'merchant':
            messages.warning(request,"Invalid Request")
            return redirect('dashboard')

        farmer = FarmerProfile.objects.get(user = user)

        
        crop = Crop()
        crop.crop_name = crop_name
        crop.farmer = farmer
        crop.crop_image = image
        crop.crop_desc = description
        crop.stock = stock
        crop.price = base_price
        crop.is_available = True
        crop.save()

        slug = crop_name + str(user.id) + str(crop.id)
        crop.slug = slug
        crop.save()

        messages.info(request,"Your Crop has been Sucessfully uploaded!!")
        return redirect('dashboard')
    return render(request,'crops/upload_crop.html')



def view_crops(request):
    user = request.user
    if user.profile == 'merchant':
        messages.warning(request,"Invalid Request")
        return redirect('dashboard')

    farmer = FarmerProfile.objects.get(user=user)

    crops = Crop.objects.filter(farmer=farmer)

    data = {
        'crops' : crops
    }

    return render(request,'crops/view_crops.html',data)
    


        







