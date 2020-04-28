from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def tutoring(request):
    students = Student.objects.all()
    output = "The students are "

    for student in students:
        output += f"{student.first_name}, and "

    output += "that's it."
        
    return HttpResponse(output)
