from sqlite3 import Timestamp
from django.db import models
from django.forms import ImageField
import uuid
from django.contrib.auth.models import User
# Create your models here.
def uploadimage(instance,filename):
    return f'item_{instance.item_id}/{filename}'
class item(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title= models.CharField(max_length=225,null=True,blank=True,default=None)
    desc=models.TextField(default=None,null=True,blank=True)
    category = models.CharField(max_length=225,default=None)
    image=models.ImageField(default=None,upload_to=uploadimage)
    price=models.IntegerField(default=None)
    added_to_cart = models.BooleanField(default=False)
    stock=models.IntegerField(default=None)
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fooditem = models.ForeignKey(item,on_delete=models.CASCADE,to_field='item_id')
    quantity = models.IntegerField(default=None)
    TotalPrice = models.IntegerField(default=None)
    class Meta:
        default_permissions = ('view',)