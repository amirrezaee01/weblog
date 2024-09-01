from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect




# Create your views here.
from django.http import HttpResponseRedirect

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to the next parameter if it exists
                    next_url = request.POST.get('next')
                    if next_url:
                        return HttpResponseRedirect(next_url)
                    else:
                        return redirect('/')
    
        else:
            form = AuthenticationForm()
            # Pass the next parameter to the template if it exists
            next_url = request.GET.get('next', '/')
        
        context = {'form': form, 'next': next_url}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

        
@login_required
def logout_view(request):

    logout(request) 
    return redirect('/')
    
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('accounts:login')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = UserCreationForm()
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')