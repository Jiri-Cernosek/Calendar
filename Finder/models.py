from django.db import models

class SalesManager(models.Model):
    manager_name = models.CharField(max_length = 30)

    def __str__(self):
        return "{0}".format(self.manager_name)

    class Meta:
        verbose_name="Manager"
        verbose_name_plural="Managers"


class PostalCode(models.Model):
    city = models.CharField(max_length = 20)
    district = models.CharField(max_length = 20)
    region = models.CharField(max_length = 20)
    code = models.IntegerField()

    def __str__(self):
        return "City: {0} | Postal code: {1}".format(self.city, self.code)

    class Meta:
        verbose_name="Postal code"
        verbose_name_plural="Postal codes"


class Customer(models.Model):
    manager = models.ForeignKey(SalesManager, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    postal_code = models.ForeignKey(PostalCode, on_delete = models.RESTRICT)
    address = models.CharField(max_length = 250)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name="Customer"
        verbose_name_plural="Customers"
