from django.contrib import admin
from .models import Category, Service, Booking, Payment

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Payment)    
# Register your models here.
