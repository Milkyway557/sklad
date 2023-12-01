from django.contrib import admin
from .models import Measure,nameOfItem,Commodity,OutWareHouse,Personal,history
# Register your models here

admin.site.register(Measure)
admin.site.register(nameOfItem)
admin.site.register(Commodity)
admin.site.register(OutWareHouse)
admin.site.register(Personal)
admin.site.register(history)