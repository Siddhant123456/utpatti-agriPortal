from django.contrib import admin
from .models import Crop,Category,MerchantCrop
# Register your models here.


admin.site.register(Crop)
admin.site.register(Category)

admin.site.register(MerchantCrop)