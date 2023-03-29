from django.urls import path,re_path
from contacts.views import index,get_contacts


app_name = 'contacts'

urlpatterns = [

    path('get_contacts/', view= get_contacts, name='get_contacts'),
    path('', view = index, name='index'),

]

