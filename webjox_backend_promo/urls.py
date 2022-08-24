from django.urls import path
from .views import *

urlpatterns = [
    path('', PromoAPIList.as_view()),
]