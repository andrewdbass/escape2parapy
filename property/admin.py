from django.contrib import admin
from property.models import Property, PropertyImage, Review, SpecialRate, Booking, UnavailableDate

# admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Review)
admin.site.register(SpecialRate)
admin.site.register(Booking)
admin.site.register(UnavailableDate)


class PropertyImageAdminInline(admin.TabularInline):
    model = PropertyImage

class ReviewAdminInline(admin.TabularInline):
    model = Review

class SpecialRateAdminInline(admin.TabularInline):
    model = SpecialRate

class BookingAdminInline(admin.TabularInline):
    model = Booking

class UnavailableDateInline(admin.TabularInline):
    model = UnavailableDate

class PropertyAdmin(admin.ModelAdmin):
    inlines = (PropertyImageAdminInline, ReviewAdminInline, SpecialRateAdminInline, BookingAdminInline, UnavailableDateInline)
admin.site.register(Property, PropertyAdmin)
