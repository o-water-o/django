from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    out = ", ".join(['{}'.format(q.pub_date) for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(render(request, 'polls/index.html',     context))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(render(request, 'polls/detail.html', {'question': question}))
