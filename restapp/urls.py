
from django.urls import path
from .views import *


urlpatterns = [
    path('first/', firstAPI),
    path('registration/', registrationAPI),

]
