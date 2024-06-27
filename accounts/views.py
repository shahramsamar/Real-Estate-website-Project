from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_view(request):
    if not  request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS,"created user as {request.user.username}")
                    return redirect('/')
                
        return render(request, 'accounts/login.html')
        # messages.add_message(request, messages.ERROR, "user is not authenticated" )

    else:
        messages.add_message(request, messages.SUCCESS,f"user is authenticated as {request.user.username}")
        return redirect('/')

# def logout_view(request):
#         return render(request, 'accounts/register.html')

def register_view(request):
    return render(request, 'accounts/register.html')