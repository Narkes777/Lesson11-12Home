from django.urls import path
from .views import students_by_course

urlpatterns = [
    path('course/<int:course_id>/students/', students_by_course, name='students_by_course'),
]
