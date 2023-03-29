from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from Register_Login.views import create_users_API,login_users_API,get_user_by_email,notification_tokens


app_name = 'Register_Login'

urlpatterns = [



    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # APIs URL
    path('create_users_API/', view= create_users_API, name='create_users_API'),
    path('login_users_API/', view= login_users_API, name='login_users_API'),
    path('get_user_by_email/<str:email>', view= get_user_by_email, name='get_user_by_email'),

    path('notification_tokens', view= notification_tokens, name='notification_tokens'),
]



