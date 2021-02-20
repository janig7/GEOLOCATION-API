from rest_framework import serializers
from geolocation.models import Geolocation
from services.ipstack import IPStack



class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = (
            'ip_address',
            'url_address',
            'city',
            'country',
            'longitude',
            'latitude',
        )


class CreateGeolocationByIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ('ip_address',)

    @staticmethod
    def _insert_data(geo_data, instance, ip_address=None, url_address=None):
        instance.ip_address = ip_address
        instance.url_address = url_address
        instance.country = geo_data['country']
        instance.city = geo_data['city']
        instance.longitude = geo_data['longitude']
        instance.latitude = geo_data['latitude']
        return

    @staticmethod
    def _get_geo_data(ip_address=None, url_address=None):
        ip_stack = IPStack(ip=ip_address, url=url_address)
        return ip_stack.get_data()

    def create(self, validated_data):
        ip_address = validated_data.pop('ip_address', None)
        instance = self.Meta.model(**validated_data)
        if Geolocation.objects.filter(ip_address=ip_address).exists():
            return False
        else:
            geo_data = self._get_geo_data(ip_address=ip_address)
            self._insert_data(geo_data, instance, ip_address=ip_address)
            instance.save()

        return instance


class CreateGeolocationByURNSerializer(CreateGeolocationByIPSerializer):
    class Meta:
        model = Geolocation
        fields = ('url_address',)

    def create(self, validated_data):
        url_address = validated_data.pop('url_address', None)
        instance = self.Meta.model(**validated_data)
        if Geolocation.objects.filter(url_address=url_address).exists():
            return False
        else:
            geo_data = self._get_geo_data(url_address=url_address)
            self._insert_data(geo_data, instance, url_address=url_address)
            instance.save()

        return instance
