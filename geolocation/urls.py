from django.urls import path
from django.views.generic import TemplateView

app_name = 'geolocation'

urlpatterns = [
	path('', TemplateView.as_view(template_name='geolocation/index.html')),
]
