from property.models import Property, PropertyImage, Review, SpecialRate, Booking, UnavailableDate
from property.serializers import PropertySerializer, PropertyImageSerializer, ReviewSerializer, SpecialRateSerializer, BookingSerializer, UnavailableDateSerializer
from rest_framework import viewsets

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SpecialRateViewSet(viewsets.ModelViewSet):
    queryset = SpecialRate.objects.all()
    serializer_class = SpecialRateSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UnavailableDateViewSet(viewsets.ModelViewSet):
    queryset = UnavailableDate.objects.all()
    serializer_class = UnavailableDateSerializer
