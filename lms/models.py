from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    ROLE_CHOICES = [
        ('VSO', 'VSO'),
        ('Trainer', 'Trainer'),
        ('Admin', 'Admin'),
    ]
    
    STATUS_CHOICES = [
        ('Speed Sign-off', 'Speed Sign-off'),
        ('Double Cab', 'Double Cab'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    employee_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    # Additional fields for managing other information
    initial_training_records = models.TextField(blank=True)
    investigations = models.TextField(blank=True) 
    pcn_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# QA Report model
class QAReport(models.Model):
    RESULT_CHOICES = [
        ('Red', 'Red'),
        ('Amber', 'Amber'),
        ('Green', 'Green'),
    ]
    
    report_title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    report_reference = models.CharField(max_length=100, unique=True)
    reference_link = models.URLField(max_length=200, blank=True, null=True)
    result = models.CharField(max_length=5, choices=RESULT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qa_reports')

    def __str__(self):
        return f"{self.report_title} - {self.user.username}"
    
    # Method to filter previous, latest, and upcoming reports
    @staticmethod
    def get_reports(user):
        today = timezone.now().date()
        previous_reports = QAReport.objects.filter(user=user, date__lt=today)
        latest_report = QAReport.objects.filter(user=user).order_by('-date').first()
        upcoming_reports = QAReport.objects.filter(user=user, date__gt=today)

        return {
            'previous': previous_reports,
            'latest': latest_report,
            'upcoming': upcoming_reports,
        }
