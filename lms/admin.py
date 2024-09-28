from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, QAReport, TrainingRecord

# Profile inline for User model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Unregister the default User model and re-register with Profile inline
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register QAReport model
@admin.register(QAReport)
class QAReportAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'date', 'report_reference', 'reference_link', 'result', 'user')
    search_fields = ('report_title', 'report_reference', 'reference_link', 'user__username')
    list_filter = ('result', 'user', 'date')

# Customizing the TrainingRecord admin to display both file and URL options
@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('training_title', 'training_type', 'date', 'status', 'get_document', 'user')
    search_fields = ('training_title', 'user__username')
    list_filter = ('training_type', 'status', 'date', 'user')
    date_hierarchy = 'date'
    list_per_page = 20

    # Custom method to show either the URL or file in the admin panel
    def get_document(self, obj):
        if obj.supporting_document_url:
            return f"URL: {obj.supporting_document_url}"
        elif obj.supporting_document:
            return f"File: {obj.supporting_document.name}"
        else:
            return "No document"
    get_document.short_description = 'Document'
