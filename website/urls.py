from website.views import *
from django.urls import path,include


urlpatterns = [
    path('',index_view),
    path('about',about_view),
    path('contact',contact_view),
    path('login',login_view),
    path('signup',signup_view),
]