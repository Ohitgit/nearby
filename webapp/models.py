from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
import math
# Create your models here.
class Profile(models.Model):
      user=models.OneToOneField(User,related_name='user_name',on_delete=models.CASCADE)
      pincode=models.IntegerField(default=0,db_index=True)
      city=models.CharField(max_length=100,null=True,blank=True)
      address=models.TextField(null=True,blank=True)
      created = models.DateTimeField(auto_now_add=True)
      updated = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.user

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    img=models.FileField(upload_to='images/',db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=255,null=True,blank=True,db_index=True) 
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.city
    
class SubLocation(models.Model):
    area = models.CharField(max_length=255,null=True,blank=True,db_index=True) 
    location= models.ForeignKey(Location,related_name='sublocations',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.area


class Business_Detalies(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True,db_index=True) 
    slug = models.SlugField(blank=True)
    user= models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    img=models.FileField(upload_to='category/',db_index=True,null=True,blank=True)
    location= models.ForeignKey(SubLocation,related_name='locations',on_delete=models.CASCADE)
    city= models.ForeignKey(Location,related_name='citys',on_delete=models.CASCADE,null=True,blank=True)
    category= models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    address=models.TextField(null=True,blank=True)
    pincode=models.IntegerField(default=0)
    state = models.CharField(max_length=255,null=True,blank=True,db_index=True)
    open_time=models.CharField(max_length=255,null=True,blank=True,db_index=True)
    close_time=models.CharField(max_length=255,null=True,blank=True,db_index=True)
    latitude=models.FloatField(default=0)
    longtitude=models.FloatField(default=0)
    distance=models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            counter = 1
            base_slug = self.slug
            while Business_Detalies.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

def calculate_distance(lat1, lon1, lat2, lon2):
    # Haversine formula
    R = 6371  # Earth radius in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Distance in kilometers

@receiver(post_save, sender=Business_Detalies)
def update_distance(sender, instance, **kwargs):
    reference_lat = 22.7196
    reference_lon = 75.8577

    distance = calculate_distance(reference_lat, reference_lon, instance.latitude, instance.longtitude)

    # Only update if value changed
    if instance.distance != distance:
        instance.distance = distance
        instance.save(update_fields=['distance'])
class EnquiryForm(models.Model):
      name=models.CharField(max_length=200,null=True,blank=True,db_index=True)
      mobile=models.IntegerField(default=0)
      business= models.ForeignKey(Business_Detalies,related_name='business',on_delete=models.CASCADE)
       
      def __str__(self):
         return  self.name