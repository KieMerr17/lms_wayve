from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Profile(models.Model):
    ROLE_CHOICES = [
        ('VSO', 'VSO'),
        ('Trainer', 'Trainer'),
        ('QA', 'QA'),
        ('Admin', 'Admin'),
    ]
    
    STATUS_CHOICES = [
        ('On-road Testing', 'On-road Testing'),
        ('Refresher required', 'Refresher required'),
        ('Off road', 'Off road'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    employee_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On-road Testing')
    
    # Additional fields for managing other information
    initial_training_records = models.TextField(blank=True)
    investigations = models.TextField(blank=True) 
    pcn_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return f"{self.user.username} - {self.role}"


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


class TrainingRecord(models.Model):
    TRAINING_TYPE_CHOICES = [
        ('Initial', 'Initial'),
        ('Refresher', 'Refresher'),
        ('Advanced', 'Advanced'),
    ]
    
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_records')
    training_title = models.CharField(max_length=200)
    training_type = models.CharField(max_length=20, choices=TRAINING_TYPE_CHOICES)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    # Remove the supporting_document field
    supporting_document_url = models.URLField(max_length=500, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.training_title} - {self.user.username} - {self.status}"

    def clean(self):
        """
        Ensure that a URL is provided.
        """
        if not self.supporting_document_url:
            raise ValidationError("You must provide a URL for the supporting document.")

    @staticmethod
    def get_training_records(user):
        """
        Fetches and returns all training records for the specified user, ordered by the latest date first.
        """
        return TrainingRecord.objects.filter(user=user).order_by('-date')
