from rest_framework import serializers
from property.models import Property, PropertyImage, Review, SpecialRate, Booking, UnavailableDate
import datetime
from rest_framework.response import Response
from rest_framework import status

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        depth = 1
        fields = ('id','created', 'title', 'default_rate', 'spring_rate',
        'summer_rate', 'fall_rate', 'winter_rate', 'guests', 'beds',
        'baths', 'description', 'amenities', 'house_rules', 'address',
        'images', 'reviews', 'special_rates', 'bookings', 'unavailable_dates', 'map_embed_src')

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SpecialRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialRate
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    def validate(self, data):
        d = data['start_date']
        delta = datetime.timedelta(days=1)
        while d < data['end_date']:
            print(d.strftime("%Y-%m-%d"))
            if UnavailableDate.objects.filter(date=d, prop=data['prop']).exists():
                raise serializers.ValidationError("Date Range contains unavailable_dates")
            d += delta
        return data
    def create(self, validated_data):
        booking = Booking.objects.create(**validated_data)
        d = booking.start_date
        delta = datetime.timedelta(days=1)
        while d < booking.end_date:
            print(d.strftime("%Y-%m-%d"))
            UnavailableDate.objects.create(date=d, prop=booking.prop, booking=booking)
            d += delta
        return booking


class UnavailableDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnavailableDate
        fields = '__all__'
