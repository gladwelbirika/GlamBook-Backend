from django.contrib import admin
from .models import Category, Service, Booking, Payment, Stylist

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Payment)  
admin.site.register(Stylist)  
# Register your models here.
