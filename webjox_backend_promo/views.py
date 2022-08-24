from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SiteSerializer
from .models import Site

class PromoAPIList(generics.GenericAPIView):
    serializer_class = SiteSerializer

    def get(self, request, *args, **kwargs):
        queryset = Site.objects.all().first()
        data = self.serializer_class(queryset).data
        return Response(data=data, status=status.HTTP_200_OK)
