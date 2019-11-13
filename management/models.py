from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=200,blank=False)
    price = models.IntegerField(blank=False)
    discount = models.IntegerField(blank=True)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'Services'
        verbose_name_plural= 'Services'

class CarBrand(models.Model):
    brandName = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.brandName
    
    class Meta:
        verbose_name = 'Car Brands'
        verbose_name_plural = 'Car Brands'


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    modelName = models.CharField(max_length=200)

    def __str__(self):
        return self.modelName+' - '+self.brand.brandName
    
    class Meta:
        verbose_name='Car Models'
        verbose_name_plural = 'Car Models'


class Application(models.Model):
    applicationID = models.CharField("Application ID",max_length=20,blank=False)
    userID = models.ForeignKey(User,on_delete=models.CASCADE)
    carBrand = models.ForeignKey(CarBrand,on_delete=models.CASCADE)
    carModel = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    vehicleNumber = models.CharField("Vehicle Number",max_length=100, blank=False)
    serviceType = models.ForeignKey(Service,on_delete=models.CASCADE)
    date = models.DateTimeField("Date",auto_now_add=True)
    Applied = 'Applied'
    Recieved = 'Recieved'
    Confirmed = 'Confirmed'
    state = [(Applied, 'Applied'),(Recieved, 'Recieved'),(Confirmed, 'Confirmed')]
    status = models.CharField("Status",max_length=20,choices=state,default=Applied)

    def __str__(self):
        return self.applicationID
    
    class Meta:
        verbose_name = 'Applications'
        verbose_name_plural = 'Applications'