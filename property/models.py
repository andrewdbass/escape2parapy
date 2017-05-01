from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Property(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')

    default_rate = models.IntegerField()
    spring_rate = models.IntegerField()
    summer_rate = models.IntegerField()
    fall_rate = models.IntegerField()
    winter_rate = models.IntegerField()

    guests = models.IntegerField()
    beds = models.IntegerField()
    baths = models.IntegerField()

    description = models.TextField()
    amenities = models.TextField()
    house_rules = models.TextField()

    address = models.CharField(max_length=600, blank=False, default='')

    class Meta:
        ordering = ('created',)

class PropertyImage(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    text = models.CharField(max_length=100, blank=True, default='')
    position = models.IntegerField()

class Review(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()

class SpecialRate(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='special_rates')
    date = models.DateField()
    rate = models.IntegerField()

class Booking(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    # customer = idont know how to handle stripe in django
    customer_email = models.EmailField(max_length=254)

class UnavailableDate(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='unavailable_dates')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True)
    date = models.DateField()
