from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication



class TalabalarViewSet(viewsets.ModelViewSet):
    queryset = Talabalar.objects.all()
    serializer_class = TalabalarSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['ismi','familiyasi']
    search_fields = ['ismi','familiyasi']
    ordering_fields = ['ismi']
    ordering = ['-id']


class LoyihaViewSet(viewsets.ModelViewSet):
    queryset = Loyiha.objects.all()
    serializer_class = LoyihaSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
   




# Create your views here.
