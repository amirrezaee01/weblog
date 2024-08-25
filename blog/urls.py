from blog.views import *
from django.urls import path,include

app_name = "blog"

urlpatterns = [
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_view,name='category'),    
    path('author/<str:author_username>',blog_view,name='author'),    
]  