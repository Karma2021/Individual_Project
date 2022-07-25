from datetime import date, datetime
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image=models.FileField(upload_to="static/images",default="default.jpg")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    productBrand = models.CharField(max_length=255,default="")
    name = models.CharField(max_length=255, default="")
    price = models.FloatField()
    quantity = models.CharField(max_length=10)
    address = models.TextField()
    phonenumber=models.CharField(max_length=100)
    pincode=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    payment=models.CharField(max_length=255,default="")
    total=models.CharField(max_length=10000, default="")
    date=models.DateField(default=datetime.today)



    class Meta:
        db_table="Order"
        verbose_name_plural = 'Order'