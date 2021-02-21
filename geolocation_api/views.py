from .serializers import (
    GeolocationSerializer,
    CreateGeolocationByIPSerializer,
    CreateGeolocationByURNSerializer,
)
from rest_framework.permissions import IsAuthenticated
from geolocation.models import Geolocation
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.settings import api_settings


class GeolocationBaseView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all()

    def retrieve(self, request, *args, **kwargs):
        ip_serializer = CreateGeolocationByIPSerializer(data=kwargs)
        ip_serializer.is_valid(raise_exception=True)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        create_serializer = CreateGeolocationByIPSerializer(data=kwargs)
        create_serializer.is_valid(raise_exception=True)
        create_serializer.save()
        headers = self.get_success_headers(create_serializer.data)
        return Response(
            create_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def destroy(self, request, *args, **kwargs):
        delete_serializer = CreateGeolocationByIPSerializer(data=kwargs)
        delete_serializer.is_valid(raise_exception=True)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class GeolocationDetail(GeolocationBaseView):
    lookup_field = 'ip_address'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self.get(request, *args, **kwargs))
