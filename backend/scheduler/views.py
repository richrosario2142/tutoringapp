from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tutoring(request):
    return HttpResponse('We in da buildin')
