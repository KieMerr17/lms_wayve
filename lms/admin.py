from django.contrib import admin
from .models import Course, QAReport

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active')
    search_fields = ('title', 'description', 'instructor__username')
    list_filter = ('start_date', 'end_date', 'is_active')
    

@admin.register(QAReport)
class QAReportAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'date', 'report_reference', 'reference_link', 'result', 'user') 
    search_fields = ('report_title', 'report_reference', 'reference_link', 'user__username') 
    list_filter = ('result', 'user', 'date')
