# Importing Django Libraries required
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import update_last_login


# Rest Libraries
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Register_Login.serializers import LoginSerializer, UserSerializer,TokenSerializer
from django.http import JsonResponse


# Importing setting from the main project


# Importing Models
from Register_Login.models import AccessToken,Notification_token,Push_Notification, Events, Profile, Team_Member

# from cart_and_orders.models import Cart

# Importing Forms
from Register_Login.forms import Event_form, LoginForm, RegisterForm


# Firebase Libraries

# import firebase_admin
# from firebase_admin import messaging, credentials

# cred = credentials.Certificate("x-eats-15a80-firebase-adminsdk-atk3a-fffd7ed32a.json")
# firebase_admin.initialize_app(cred)


# firebaseConfig = {
#     'apiKey': "AIzaSyAaS25sOWbMamSpdrhumzoim8z15ctoJsM",
#     'authDomain': "x-eats-15a80.firebaseapp.com",
#     'projectId': "x-eats-15a80",
#     'storageBucket': "x-eats-15a80.appspot.com",
#     'messagingSenderId': "258167260360",
#     'appId': "1:258167260360:web:59fef311d6cc809c8391fd",
#     'measurementId': "G-6FLQ8JHVN8"
# }




# APIs Handling   
# Creating Users
@csrf_exempt 
@api_view(['GET','POST'])
def create_users_API(request):
    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            user = Profile.objects.create_user(
                    email=request.data['email'],
                    first_name=request.data['first_name'],
                    last_name=request.data['last_name'],
                    password=request.data['password'],
                    title=serializer.validated_data['title'],
                    PhoneNumber=request.data['PhoneNumber'],
                    is_active = True
                )
            if user:
                return Response("User Created Successfully", status = status.HTTP_201_CREATED)
            else:
                return Response("Error Creating User", status = status.HTTP_403_FORBIDDEN)
        else:
            return Response("Serializer Not Valid", status = status.HTTP_400_BAD_REQUEST)

# Login Users
@csrf_protect
@api_view(['GET','POST','PUT'])
def login_users_API(request):
    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True)
        serializer = LoginSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = LoginSerializer(data= request.data,context={'request': request})
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("Valid")
            user = authenticate(request, email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
            )
            if user:
                if user.is_active:
                        update_last_login(None, user)
                        user_login(request, user)
                        print('active')
                        print(HttpResponse.status_code)
                        return Response(status = status.HTTP_302_FOUND)

                else:
                    print('Not Active')
                    return Response.status_code
           
            else:
                print('Invalid Credentials')
                print(status.HTTP_404_NOT_FOUND)
                return Response(status = status.HTTP_404_NOT_FOUND)
                
        else:
            print("Not Valid")
        return Response(serializer.data, status = status.HTTP_404_NOT_FOUND)

# Get User by Id
@api_view(['GET','POST','PUT'])
def get_user_by_email(request,email):
    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True,email=email)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['POST'])
def logout(request,email):
    if request.method == 'GET':
        return JsonResponse('No Response', safe=False)
    if request.method == 'POST':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            logout()
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
            

# Get Notification token
@api_view(['GET','POST'])
def notification_tokens(request):
    if request.method == 'GET':
        all = Notification_token.objects.all()
        serializer = TokenSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = TokenSerializer(data= request.data)
        if Notification_token.objects.filter(token=request.data['token']).exists():
            return Response('Exist', status = status.HTTP_302_FOUND)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            
            