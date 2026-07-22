from rest_framework import serializers
from .models import Category, Service, Stylist, Booking, Payment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class StylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stylist
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate_date(self, value):
        from django.utils import timezone

        if value < timezone.now().date():
            raise serializers.ValidationError(
                "Booking date cannot be in the past."
            )

        return value

    def validate(self, data):
        stylist = data.get("stylist")
        date = data.get("date")
        time = data.get("time")

        existing_booking = Booking.objects.filter(
            stylist=stylist,
            date=date,
            time=time
        )

        if self.instance:
            existing_booking = existing_booking.exclude(
                id=self.instance.id
            )

        if existing_booking.exists():
            raise serializers.ValidationError(
                "This stylist already has a booking at this date and time."
            )

        return data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"