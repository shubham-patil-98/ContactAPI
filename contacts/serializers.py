from django.db import models
from rest_framework import  serializers
from .models import Contact

class ContactSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contact
        fields=('__all__')
