from django.urls import path, re_path
from .views import GeolocationDetail, CreateGeolocation, DestroyGeolocation, GeolocationURLDetail, CreateGeolocationByURN
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)

app_name = 'geolocation_api'

urlpatterns = [
	path('ip/<str:ip_address>/', GeolocationDetail.as_view(), name='detailgeolocation'),
	path('url/<str:url_address>/', GeolocationURLDetail.as_view(), name='urldetailgeolocation'),
	path('create/ip/<str:ip_address>/', CreateGeolocation.as_view(), name='creategeolocation'),
	path('create/url/<str:url_address>/', CreateGeolocationByURN.as_view(), name='creategeolocation'),
	path('delete/ip/<str:ip_address>/', DestroyGeolocation.as_view(), name='destorygeolocation'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
