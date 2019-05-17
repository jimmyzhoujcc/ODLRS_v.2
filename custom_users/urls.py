from django.urls import path
from django.contrib.auth import views as auth_views

from .views import profile, profile_update


app_name = 'custom_users'

urlpatterns = [

    # path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile-update'),

    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

]

