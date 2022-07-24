from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    book_name = models.CharField(max_length=255,blank=True)
    book_price = models.FloatField(blank=True)
    book_des = models.CharField(max_length=2000,blank=True)
    book_stock = models.CharField(max_length=255,blank=True)
    prod_cat = models.CharField(max_length=255,blank=True)
    book_image=models.FileField(upload_to="static/images",default="default.jpg")

    class Meta:
        db_table = 'product'
