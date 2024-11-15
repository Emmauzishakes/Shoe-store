from django.shortcuts import render, redirect
from .forms import CreateUser, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def RegistaionView(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()

            return redirect('userauth:login')
        
    return render(request, "userauth/registration.html", {
        'form': form
    })

def LoginView(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=username, email=email, password=password)

            if user is not None:
                login(request, user)
                print("logged in successfuly!")

                return redirect("customer:home")

    return render(request, "userauth/login.html", {
        'form': form
    })

def LogoutView(request):
    logout(request)

    return redirect('customer:home')