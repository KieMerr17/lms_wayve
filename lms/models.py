from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.title

class QAReport(models.Model):
    RESULT_CHOICES = [
        ('Red', 'Red'),
        ('Amber', 'Amber'),
        ('Green', 'Green'),
    ]

    report_title = models.CharField(max_length=200) 
    date = models.DateField(auto_now_add=True)
    report_reference = models.CharField(max_length=100, unique=True)
    result = models.CharField(max_length=5, choices=RESULT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qa_reports')  # User associated with the report

    def __str__(self):
        return f"{self.report_title} - {self.user.username}"