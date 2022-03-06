from django.db import models

class SalesManager(models.Model):
    ManagerName = models.CharField(max_length = 30)

class PostalCode(models.Model):
    City = models.CharField(max_length = 20)
    District = models.CharField(max_length = 20)
    Region = models.CharField(max_length = 20)
    Code = models.IntegerField()

class Customer(models.Model):
    CustomerManager = models.ForeignKey(SalesManager, on_delete = models.CASCADE)
    CustomerName = models.CharField(max_length = 50)
    CustomerPostalCode = models.ForeignKey(PostalCode, on_delete = models.CASCADE)
    CustomerAddress = models.CharField(max_length = 250)

