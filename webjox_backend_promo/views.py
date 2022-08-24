from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SiteSerializer, HeaderSerializer, MainBlockSerializer, OurServicesSerializer, InterviewSerializer, KeysesSerializer, FeedbacksSerializer, CooperationFormatsSerializer, LeadFormSerializer, FooterSerializer
from .models import Site, Header, MainBlock, OurServices, Interview, Keyses, Feedbacks, CooperationFormats, LeadForm, Footer

class PromoAPIList(generics.GenericAPIView):
    serializer_class = SiteSerializer

    def get(self, request, *args, **kwargs):
        queryset = Site.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoHeaderAPIList(generics.GenericAPIView):
    serializer_class = HeaderSerializer

    def get(self, request, *args, **kwargs):
        queryset = Header.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoMainBlockAPIList(generics.GenericAPIView):
    serializer_class = MainBlockSerializer

    def get(self, request, *args, **kwargs):
        queryset = MainBlock.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoOurServicesAPIList(generics.GenericAPIView):
    serializer_class = OurServicesSerializer

    def get(self, request, *args, **kwargs):
        queryset = OurServices.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoInterviewAPIList(generics.GenericAPIView):
    serializer_class = InterviewSerializer

    def get(self, request, *args, **kwargs):
        queryset = Interview.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoKeysesAPIList(generics.GenericAPIView):
    serializer_class = KeysesSerializer

    def get(self, request, *args, **kwargs):
        queryset = Keyses.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoFeedBacksAPIList(generics.GenericAPIView):
    serializer_class = FeedbacksSerializer

    def get(self, request, *args, **kwargs):
        queryset = Feedbacks.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoCooperationFormatsAPIList(generics.GenericAPIView):
    serializer_class = CooperationFormatsSerializer

    def get(self, request, *args, **kwargs):
        queryset = CooperationFormats.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoLeadFormAPIList(generics.GenericAPIView):
    serializer_class = LeadFormSerializer

    def get(self, request, *args, **kwargs):
        queryset = LeadForm.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)


class PromoFooterAPIList(generics.GenericAPIView):
    serializer_class = FooterSerializer

    def get(self, request, *args, **kwargs):
        queryset = Footer.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)
