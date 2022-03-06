from django.contrib import admin
from .models import SalesManager, Customer, PostalCode

admin.site.register(SalesManager)
admin.site.register(Customer)
admin.site.register(PostalCode)
