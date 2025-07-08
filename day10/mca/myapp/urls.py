from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_student,name='insert_student'),
    # other paths as needed
]
