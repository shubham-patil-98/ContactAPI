from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializers
from .models import Contact
from .mypagination import MyPageNumberPagination
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

class Contactviewset(viewsets.ModelViewSet):
    queryset=Contact.objects.all().order_by('name')
    serializer_class=ContactSerializers
    pagination_class=MyPageNumberPagination
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[DjangoObjectPermissions]
