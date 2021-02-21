from django.urls import path
from .views import GeolocationDetail
from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)

app_name = 'geolocation_api'

urlpatterns = [
	path('ip/<str:ip_address>/', GeolocationDetail.as_view(), name='detailgeolocation'),
	# path('url/<str:url_address>/', GeolocationURLDetail.as_view(), name='urldetailgeolocation'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
