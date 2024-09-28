from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, QAReport

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
