from django.contrib import admin
from geolocation.models import Geolocation


@admin.register(Geolocation)
class GeolocationAdmin(admin.ModelAdmin):
	list_display = ['url_address', 'city', 'country', 'longitude', 'latitude']