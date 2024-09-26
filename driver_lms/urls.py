from django.contrib import admin
from django.urls import path
from lms.views import login_view, signup_view, dashboard_view, qa_reports_view

urlpatterns = [
    path('', login_view, name='login'),
    path('qa-reports/', qa_reports_view, name='qa_reports'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    path('admin/', admin.site.urls),
]
