from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Stylist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} with {self.stylist.name} on {self.date} at {self.time}"
    
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.booking}"