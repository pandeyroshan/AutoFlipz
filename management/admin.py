from django.contrib import admin
from .models import Service, Application, CarBrand, CarModel
# Register your models here.

admin.site.register(Service)
admin.site.register(Application)
admin.site.register(CarBrand)
admin.site.register(CarModel)