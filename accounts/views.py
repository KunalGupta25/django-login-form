from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from .models import CustomUser  # Import your custom user model


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if isinstance(user, CustomUser):
                if user.user_type == 'Patient':
                    return redirect('patient_dashboard')
                if user.user_type == 'Doctor':
                    return redirect('doctor_dashboard')
                msg = 'User type not recognized.'
            else:
                msg = 'Invalid user type.'
        else:
            msg = 'Invalid credentials'
    return render(request, 'login.html', {'msg': msg})


def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})


def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})
