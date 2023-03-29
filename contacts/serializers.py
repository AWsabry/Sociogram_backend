from rest_framework import serializers
from contacts.models import Contacts



class Contacts_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name',"PhoneNumber", "onApp", 'created',]
