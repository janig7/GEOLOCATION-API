from django.db import models
from core.settings import AUTH_USER_MODEL
# from django.contrib.gis.db import models
from .validator import validate_urn


class Geolocation(models.Model):
	ip_address = models.GenericIPAddressField(null=True, blank=True)
	url_address = models.CharField(max_length=255, validators=[validate_urn], null=True)
	city = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	longitude = models.DecimalField(max_digits=25, decimal_places=8, null=True)
	latitude = models.DecimalField(max_digits=25, decimal_places=8, null=True)
