from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from lms.views import login_view, signup_view, dashboard_view, qa_reports_view, training_records_view

urlpatterns = [
    path('', login_view, name='login'),
    path('qa-reports/', qa_reports_view, name='qa_reports'),
    path('training-records/', training_records_view, name='training_records'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)