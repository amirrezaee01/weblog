from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')
    
    
def contact_view(request):
    return render(request,'website/contact.html')

def login_view(request):
    return render(request,'accounts/login.html')
def signup_view(request):
    return render(request,'accounts/signup.html')