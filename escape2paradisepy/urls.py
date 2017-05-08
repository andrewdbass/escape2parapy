
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

from django.conf.urls.static import static
from django.conf import settings

from property import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/properties', views.PropertyViewSet, "property")
router.register(r'api/booking', views.BookingViewSet)
router.register(r'unavailable-date', views.UnavailableDateViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^properties/$', views.PropertyViewSet),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
