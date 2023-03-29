from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from contacts.models import Contacts
from contacts.serializers import Contacts_serializer


# Create your views here.


def index(request):
    return render(request, "index.html")




@api_view(['GET','POST'])

# Getting the Contacts from App
def get_contacts(request):
    if request.method == 'GET':
        all = Contacts.objects.all()
        serializer = Contacts_serializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = Contacts_serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
