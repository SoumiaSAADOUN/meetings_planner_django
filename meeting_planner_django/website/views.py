from django.shortcuts import render
from django.http import HttpResponse
from datetime import  datetime
# Create your views here.
def welcome(request):
    return HttpResponse("welcome to the meeting planner!")
def date(request):
    return HttpResponse("This page was served at "+ str(datetime.now()))
def about(request):
    return HttpResponse(" Hi welcome to my page! I'm Soumia SAADOUN")