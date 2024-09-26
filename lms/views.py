from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import QAReport

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check the credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, 'Incorrect username or password')
    
    return render(request, 'index.html')  # Render login page on GET or failed login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)  # Auto login the user after signup
                return redirect('dashboard')
        else:
            messages.error(request, 'Error creating account. Please check the details.')
    
    return render(request, 'index.html', {'form': UserCreationForm()})  # Display signup form

@login_required
def dashboard_view(request):
    """Render the main dashboard page for authenticated users."""
    return render(request, 'dashboard.html')  # Render the main dashboard page

@login_required
def qa_reports_view(request):
    # Fetch QA reports related to the logged-in user
    qa_reports = request.user.qa_reports.all()

    context = {
        'qa_reports': qa_reports,
    }
    return render(request, 'qa_reports.html', context)