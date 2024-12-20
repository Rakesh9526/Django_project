from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user




class Customer(models.Model):
    u_name=models.CharField(max_length=255)
    u_address = models.TextField()
    u_contact_number = models.CharField(max_length=15,unique=True)
    u_whatsapp_number = models.CharField(max_length=15)
    u_reffered_by =models.CharField(max_length=255,null=True) 


# class Photo(models.Model):
#     image = models.ImageField(upload_to='apply')
#     apply = models.ForeignKey('Apply', related_name='photos', on_delete=models.CASCADE)

#     def _str_(self):
#         return self.image.url


class Apply(models.Model):
    name=models.CharField(max_length=255,null=True)
    address = models.TextField(null=True)
    contact_number = models.CharField(max_length=15,null=True)
    whatsapp_number = models.CharField(max_length=15,null=True)
    reffered_by =models.CharField(max_length=255,null=True) 
    # service_by = models.CharField(max_length=225)
    service_by = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    WORK_TYPE_CHOICES=[
        ('sale','sale'),('service','service'),
    ]
    work_type=models.CharField(max_length=10,choices=WORK_TYPE_CHOICES,default=True)
    item_name_or_number = models.CharField(max_length=255,null=True)
    issue = models.TextField(blank=True,null=True) #applicable for 'services'
    photos_of_item =models.ImageField(upload_to='apply',blank=True,null=True)#option for 'services'
    estimation_document =models.FileField(upload_to='apply', null=True,blank=True)    
    estimated_price = models.CharField(max_length=255)
    estimated_date = models.DateField(null=True)
    any_other_comments = models.CharField(max_length=255,null=True,blank=True)


    def _str_(self):
        return self.name

    def str(self):
        return f"{self.nature_of_work.capitalize()} - {self.item_name_or_number}"
   


class FuelCharge(models.Model):
    technician_name = models.CharField(max_length=100)
    date = models.DateField()
    purpose = models.TextField()
    kilometers = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # apply = models.ForeignKey(Apply, on_delete=models.CASCADE,related_name='fuel_charges', blank=True,null=True)

class FoodAllowance(models.Model):
    # customer = models.ForeignKey(Apply, on_delete=models.CASCADE,default=True)
    technician_name = models.CharField(max_length=100)
    date = models.DateField()
    purpose = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class ItemPurchased(models.Model):
    # customer = models.ForeignKey(Apply, on_delete=models.CASCADE,default=True)
    date = models.DateField()
    item_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bill_photo = models.ImageField(upload_to='itempurchased')

class VendorInfo(models.Model):
    # customer = models.ForeignKey(Apply, on_delete=models.CASCADE,default=True)
    date = models.DateField()
    vendor_name = models.CharField(max_length=200)
    vendor_bill_photo = models.ImageField(upload_to='vendorinfo')
    vendor_eta = models.DateField()
    vendor_cost = models.DecimalField(max_digits=10, decimal_places=2)

class CurrentStatus(models.Model):
    # customer = models.ForeignKey(Apply, on_delete=models.CASCADE,default=True)
    date = models.DateField()
    technician_name = models.CharField(max_length=100)
    status = models.TextField()


class Technicians(models.Model):
    name=models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=225,null=True)
    password=models.CharField(max_length=225)
    confrim_password=models.CharField(max_length=255,null=True)

    def save(self, *args, **kwargs):
        if self.password != self.confrim_password:
            raise ValueError("Password do not match")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

