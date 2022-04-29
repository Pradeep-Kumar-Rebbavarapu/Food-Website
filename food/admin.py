from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','title','image','price','stock','category']

admin.site.register(Cart)