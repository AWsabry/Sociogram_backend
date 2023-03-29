from Register_Login.models import AccessToken, Newsletter, Notification_token,Profile, Team_Member
from django.contrib import admin
# from firebase_admin import messaging

# Register your models here.

# List_of_tokens = []
# all_notifications = Notification_token.objects.values_list('token',flat=True,)
# for i in all_notifications:
#     List_of_tokens.append(i)


# def sendPush(title,content, registration_token,image, dataObject=None):
    
#     # See documentation on defining a message payload.
#     message = messaging.MulticastMessage(
#         notification=messaging.Notification(
#             title= title,
#             body= content,
#             image= str(image),
#         ),
#         data=dataObject,
#         tokens= List_of_tokens
#     )

#     # Send a message to the device corresponding to the provided
#     # registration token.
#     response = messaging.send_multicast(message)
#     # Response is a message ID string.
#     print(List_of_tokens)
#     print('Successfully sent message:', response, message)



class Register(admin.ModelAdmin):
    list_filter = ("email","first_name", "last_name", "last_modified")
    list_display = ("email","first_name", 'last_name','last_modified','PhoneNumber','is_active','id'
                  )
    search_fields = ['email']



class Team_Admin(admin.ModelAdmin):
    model = Team_Member
    list_display = ('first_name','last_name','email','PhoneNumber')





class AccessTokenAdmin(admin.ModelAdmin):
    model = Profile
    fieldsets = (
        (None, {"fields": (
                'user', 'token', 'expires', 'created'
            )}),
    )
    readonly_fields = ('token','created')
    list_display = ('user', 'token', 'created')






# class pushNotiticationAdmin(admin.ModelAdmin):
#     model = Push_Notification
#     list_display = ('notification_name','title','content','created','id')

#     def save_model(self, request, obj, form, change):
#         sendPush(obj.title, obj.content, obj.image, List_of_tokens)
#         obj.save()



class NotificationTokensAdmin(admin.ModelAdmin):
    model = Notification_token
    list_display = ('created','token','id')






# admin.site.register(Push_Notification, pushNotiticationAdmin)
admin.site.register(Profile, Register)
admin.site.register(Team_Member, Team_Admin)
admin.site.register(Notification_token, NotificationTokensAdmin)


