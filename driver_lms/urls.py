from django.contrib import admin
from django.urls import path
from lms.views import hello_world_view


urlpatterns = [
    path('', hello_world_view),
    path('admin/', admin.site.urls),
]


