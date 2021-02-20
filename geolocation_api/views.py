from .serializers import GeolocationSerializer, CreateGeolocationByIPSerializer, CreateGeolocationByURNSerializer
from rest_framework.permissions import IsAuthenticated
from geolocation.models import Geolocation
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class GeolocationBaseView:
    # permission_classes = [IsAuthenticated]
    serializer_class = GeolocationSerializer
    queryset = Geolocation.objects.all()


class GeolocationDetail(GeolocationBaseView, generics.RetrieveAPIView):
    lookup_field = 'ip_address'

    def get(self, request, *args, **kwargs):
        print(kwargs)
        ip_serializer = CreateGeolocationByIPSerializer(data=kwargs)
        if ip_serializer.is_valid():
            return self.retrieve(request, *args, **kwargs)
        print(ip_serializer.is_valid())

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        create_serializer = CreateGeolocationByIPSerializer(data=kwargs)
        if create_serializer.is_valid():
            new_geolocation = create_serializer.save()
            if new_geolocation:
                return Response(f'Geolocation for ip address: {kwargs["ip_address"]} successfully added to database!', status=status.HTTP_201_CREATED)

        return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeolocationURLDetail(GeolocationBaseView, generics.RetrieveAPIView):
    lookup_field = 'url_address'

    def get(self, request, *args, **kwargs):
        request.data['url_address'] = kwargs.get('url_address')
        ip_serializer = CreateGeolocationByURNSerializer(data=request.data)

        if ip_serializer.is_valid():
            return self.retrieve(request, *args, **kwargs)

        return Response(self.serializer_class.errors, status=status.HTTP_404_NOT_FOUND)


class CreateGeolocation(GeolocationBaseView, generics.CreateAPIView):
    queryset = Geolocation.objects.values_list('ip_address')
    lookup_field = 'ip_address'

    def post(self, request, *args, **kwargs):
        create_serializer = CreateGeolocationByIPSerializer(data=kwargs)
        if create_serializer.is_valid():
            new_geolocation = create_serializer.save()
            if new_geolocation:
                return Response(f'Geolocation for ip address: {kwargs["ip_address"]} successfully added to database!', status=status.HTTP_201_CREATED)

        return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateGeolocationByURN(GeolocationBaseView, generics.CreateAPIView):
    queryset = Geolocation.objects.values_list('url_address')
    lookup_field = 'url_address'

    def post(self, request, *args, **kwargs):
        request.data['url_address'] = kwargs.get('url_address')
        create_serializer = CreateGeolocationByURNSerializer(data=request.data)
        if create_serializer.is_valid():
            new_geolocation = create_serializer.save()
            if new_geolocation:
                return Response(status=status.HTTP_201_CREATED)

        return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestroyGeolocation(GeolocationBaseView, generics.DestroyAPIView):
    lookup_field = 'ip_address'

    def delete(self, request, *args, **kwargs):
        request.data['ip_address'] = kwargs.get('ip_address')
        ip_serializer = GeolocationIPSerializer(data=request.data)
        if ip_serializer.is_valid():
            return self.destroy(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)

