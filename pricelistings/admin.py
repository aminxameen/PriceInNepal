from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'company_name', 'release_date', 'updated_on')
    search_fields = ('name', 'company_name')
    list_filter = ('release_date', 'updated_on')


admin.site.register(Product, ProductAdmin)
