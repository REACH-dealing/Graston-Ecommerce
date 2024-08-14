from django.contrib import admin
from .models import ProductCategory, Vendor,Product
# Register your models here.

admin.site.register(Vendor)
admin.site.register(ProductCategory)
admin.site.register(Product)


