from django.contrib import admin
from product.models import Product





# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','book_name','book_price','book_des','book_stock','prod_cat','book_image')

admin.site.register(Product, ProductAdmin)