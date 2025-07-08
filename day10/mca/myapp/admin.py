from django.contrib import admin

# Register your models here.

from .models import studentModel
admin.site.register(studentModel)
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
