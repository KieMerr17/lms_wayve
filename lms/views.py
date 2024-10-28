from collections import defaultdict
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import QAReport, TrainingRecord

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect username or password')
    
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Error creating account. Please check the details.')
    
    return render(request, 'index.html', {'form': UserCreationForm()})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
def qa_reports_view(request):
    # Fetch QA reports related to the logged-in user
    qa_reports = request.user.qa_reports.all()

    context = {
        'qa_reports': qa_reports,
    }
    return render(request, 'qa_reports.html', context)

@login_required
def training_records_view(request):
    # Fetch all training records related to the logged-in user
    training_records = TrainingRecord.objects.filter(user=request.user).order_by('-date')

    # Group the records by 'training_type'
    grouped_records = defaultdict(list)
    for record in training_records:
        grouped_records[record.training_type].append(record)

    # Pass the grouped records to the template
    context = {
        'training_records': dict(grouped_records),  # Convert defaultdict to a regular dict
    }
    return render(request, 'training_records.html', context)
