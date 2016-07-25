from django.shortcuts import render
from django.http      import HttpResponse

def index(request):
  return HttpResponse("Hello django! You're on the polls index!")

def detail(request, question_id):
	return HttpResponse("You are looking question %s." % question_id)

def results(request, question_id):
	return HttpResponse("You are looking the result of question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You are looking the vote of question %s." % question_id)