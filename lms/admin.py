from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Course, QAReport, Certificate

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Unregister the default User model and re-register with Profile inline
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active')
    search_fields = ('title', 'description', 'enrolled_users__username')  # Search by enrolled user as well
    list_filter = ('start_date', 'end_date', 'is_active')
    filter_horizontal = ('enrolled_users', 'certificates') 

# Register Certificate model
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'issue_date')
    search_fields = ('user__username', 'course__title')
    list_filter = ('issue_date',)

# Register QAReport model
@admin.register(QAReport)
class QAReportAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'date', 'report_reference', 'reference_link', 'result', 'user')
    search_fields = ('report_title', 'report_reference', 'reference_link', 'user__username')
    list_filter = ('result', 'user', 'date')
