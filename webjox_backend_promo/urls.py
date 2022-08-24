from django.urls import path
from .views import *

urlpatterns = [
    path('', PromoAPIList.as_view()),
    path('header/', PromoHeaderAPIList.as_view()),
    path('mainblock/', PromoMainBlockAPIList.as_view()),
    path('ourservices/', PromoOurServicesAPIList.as_view()),
    path('interview/', PromoInterviewAPIList.as_view()),
    path('keyses/', PromoKeysesAPIList.as_view()),
    path('feedbacks/', PromoFeedBacksAPIList.as_view()),
    path('cooperationformats/', PromoCooperationFormatsAPIList.as_view()),
    path('leadform/', PromoLeadFormAPIList.as_view()),
    path('footer/', PromoFooterAPIList.as_view()),
]
