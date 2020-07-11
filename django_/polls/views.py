from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	# return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)
 

def detail(request, question_id):
	# There is a shortcut for the following lines of code:
	'''
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	
	'''
	question = get_object_or_494(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	return HttpResponse(f"you're looking at the results of question {question_id}")


def vote(request, question_id):
	return HttpResponse(f"you're voting on question {question_id}")
# Create your views here.
