from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    """
    # Without shortcut
    from django.template import loader
    from django.http import HttpResponse
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render(context, request))
    """

    # With django shortcut
    return render(request, 'polls/index.html', context, status=200)


def detail(request, question_id):
    """
    # Without shortcut
    from django.http import Http404
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    """

    # With django shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', context={'question': question})


def results(request, question_id):
    response = "You're looking at the the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
