from blog.views import *
from django.urls import path,include

app_name = "blog"

urlpatterns = [
    path('',blog_view,name='index'),
    path('/single',blog_single,name='single'),
]  