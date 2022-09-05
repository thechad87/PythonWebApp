from django.contrib import admin

# This imports all of the models
from .models import *
# this adds the models tables to admin
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)