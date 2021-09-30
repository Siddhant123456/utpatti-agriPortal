from django.db import models

# Create your models here.

from account.models import FarmerProfile,UserProfile



class Category(models.Model):
    category_name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique =True) 
    description = models.TextField()
    

    def __str__(self):
        return self.category_name
    


class Crop(models.Model):
    crop_name = models.CharField(max_length=20)
    farmer = models.ForeignKey(FarmerProfile,on_delete=models.CASCADE)
    crop_image = models.ImageField(upload_to = 'crops/')
    crop_desc = models.TextField()
    slug = models.SlugField(blank=True,max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()
    is_available = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)



    def __str__(self):
        return self.crop_name



class MerchantCrop(models.Model):
    merchant = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop,on_delete=models.DO_NOTHING)

    #payment field will be added here 





class CropReview(models.Model):
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    detail = models.TextField()
    merchant = models.ForeignKey(UserProfile,on_delete= models.CASCADE)
    stars = models.FloatField()


    def __str__(self):
        return self.crop







