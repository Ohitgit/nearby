from django.db import models
from django.contrib.auth.models import User
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
    user= models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    img=models.FileField(upload_to='category/',db_index=True,null=True,blank=True)
    location= models.ForeignKey(SubLocation,related_name='locations',on_delete=models.CASCADE)
    category= models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    address=models.TextField(null=True,blank=True)
    pincode=models.IntegerField(default=0)
    state = models.CharField(max_length=255,null=True,blank=True,db_index=True)
    latitude=models.IntegerField(default=0)
    longtitude=models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name