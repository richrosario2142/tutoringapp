from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def tutoring(request):
    students = Student.objects.all()
    output = "Wuz good "

    for student in students:
        output += f"{student.first_name}, and "

    output += "Shloop Clan. Ya'll good?"
        
    return HttpResponse(output)
