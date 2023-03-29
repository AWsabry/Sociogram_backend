from django.contrib import admin
from contacts.models import Contacts

# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    list_filter = ("name", "created")
    list_display = ("name", "PhoneNumber", 'onApp', 'created',
                    )
    search_fields = ['name']

admin.site.register(Contacts,ContactsAdmin)
