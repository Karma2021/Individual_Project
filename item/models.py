from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    item_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'item'