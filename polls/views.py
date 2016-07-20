from django.shortcuts import render
from django.http      import HttpResponse

def index(request):
  return HttpResponse("Hello django! You're on the polls index!")
