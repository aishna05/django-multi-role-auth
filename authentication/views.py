from collections import defaultdict
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .forms import SignUpForm
from .models import CustomUser
from blog.models import BlogPost
from collections import defaultdict
from django.contrib.auth.decorators import login_required

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
    if request.user.is_authenticated and request.user.user_type == 'patient':
        posts = BlogPost.objects.filter(is_draft=False).select_related('author')  # Exclude draft posts

        # Group by category
        category_posts = defaultdict(list)
        for post in posts:
            category_posts[post.category].append(post)

        context = {
            'posts': posts,
            'category_posts': dict(category_posts),
        }
        return render(request, 'patient_dashboard.html', context)
    else:
        return render(request, 'no_access.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})



@login_required(login_url='login_view')  # Ensures only logged-in users can access this view
def home_redirect(request):
    user = request.user

    # Ensure the user has a `user_type` attribute
    if hasattr(user, 'user_type'):
        if user.user_type == 'doctor':
            return redirect('authentication:doctor_dashboard')
        elif user.user_type == 'patient':
            return redirect('authentication:patient_dashboard')

    # If user_type is missing or unrecognized
    return redirect('login_view')