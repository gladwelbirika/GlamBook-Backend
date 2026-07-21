from rest_framework import viewsets
from .models import Category, Service, Stylist, Booking, Payment
from .serializers import CategorySerializer, ServiceSerializer, StylistSerializer, BookingSerializer, PaymentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class StylistViewSet(viewsets.ModelViewSet):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
