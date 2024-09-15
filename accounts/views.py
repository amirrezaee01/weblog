from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.http import HttpResponseRedirect


User = get_user_model()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    next_url = request.GET.get('next', '/')

    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data.get('identifier')
            password = form.cleaned_data.get('password')

            user = None
            if identifier:  
                if '@' in identifier:
                    try:
                        user_obj = User.objects.get(email=identifier)
                        user = authenticate(username=user_obj.username, password=password)
                    except User.DoesNotExist:
                        user = None
                else:
                    user = authenticate(username=identifier, password=password)

            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', next_url)
                return HttpResponseRedirect(next_url)
            else:
                messages.error(request, 'Invalid username, email, or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomAuthenticationForm()

    context = {'form': form, 'next': next_url}
    return render(request, 'accounts/login.html', context)

@login_required
def logout_view(request):
    logout(request) 
    return redirect('/')
    
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('accounts:login')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = CustomUserCreationForm()
        
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')