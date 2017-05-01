from rest_framework import serializers
from property.models import Property, PropertyImage, Review, SpecialRate, Booking, UnavailableDate

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        depth = 1
        fields = ('id','created', 'title', 'default_rate', 'spring_rate',
        'summer_rate', 'fall_rate', 'winter_rate', 'guests', 'beds',
        'baths', 'description', 'amenities', 'house_rules', 'address',
        'images', 'reviews', 'special_rates', 'bookings', 'unavailable_dates')

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        # fields = ('id', 'prop', 'image', 'text', 'position')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = ('id', 'prop', 'image', 'name', 'text' )

class SpecialRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialRate
        # fields = ('id', 'prop', 'date', 'rate' )

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        # fields = ('id', 'prop', 'customer_email')

class UnavailableDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnavailableDate
        # fields = ('id', 'prop', 'booking', 'date' )
