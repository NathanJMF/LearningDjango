from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Created index view part of the poll app.
def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    item = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": item})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
