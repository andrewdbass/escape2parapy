from property.models import Property, PropertyImage, Review, SpecialRate, Booking, UnavailableDate
from property.serializers import PropertySerializer, PropertyImageSerializer, ReviewSerializer, SpecialRateSerializer, BookingSerializer, UnavailableDateSerializer
from rest_framework import viewsets
import datetime


class PropertyViewSet(viewsets.ModelViewSet):
    # queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        # print(self.request.search)
        # %a %B %m %Y:%H:%M:%S %Z%z

        if self.request.query_params.get('arrivalDate', None) is not None and self.request.query_params.get('departureDate', None) is not None:
            arrivalDate = datetime.datetime.strptime(self.request.query_params.get('arrivalDate', None), '%Y-%m-%dT%H:%M:%S.%fZ')
            departureDate = datetime.datetime.strptime(self.request.query_params.get('departureDate', None), '%Y-%m-%dT%H:%M:%S.%fZ')
            non = []
            d = arrivalDate
            delta = datetime.timedelta(days=1)
            while d < departureDate:
                print(d.strftime("%Y-%m-%d"))
                for date in  UnavailableDate.objects.filter(date=d):
                    if date.prop not in non:
                        non.append(date.prop.id)
                d += delta
            queryset = Property.objects.all().exclude(id__in=non)
            return queryset
        queryset = Property.objects.all()
        return queryset


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
