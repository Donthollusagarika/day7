from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

Step 4a: Set Up URL Routing
Edit jsdemo/urls.py:


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
]
