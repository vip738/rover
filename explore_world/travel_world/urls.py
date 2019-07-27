from django.urls import path
from travel_world.views import Authentication

app_name = 'travel_world'

urlpatterns = [
    path('', Authentication.as_view(), name='authentication')
]
