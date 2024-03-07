from django.shortcuts import render
from .models import Student

# Create your views here.

def students_by_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    return render(request, 'students_by_course.html', {'students': students})
