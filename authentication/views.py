from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .forms import SignUpForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f'/{user.user_type}/dashboard/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(f'/{user.user_type}/dashboard/')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return render(request, "registration/login.html", {"message": "Logged out successfully"})

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})