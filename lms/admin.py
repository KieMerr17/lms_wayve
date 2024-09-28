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

# Register TrainingRecord model
@admin.register(TrainingRecord)
class TrainingRecordAdmin(admin.ModelAdmin):
    list_display = ('training_title', 'training_type', 'date', 'status', 'user')
    search_fields = ('training_title', 'user__username')
    list_filter = ('training_type', 'status', 'date', 'user')
    date_hierarchy = 'date'
    list_per_page = 20
