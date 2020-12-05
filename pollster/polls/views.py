from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


# Get questions and displays

def index(request):
    print("INDEX")
    latest_questions_list = Question.objects.order_by('-published_date')[:5]
    context = {'latest_question_list': latest_questions_list}

    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
    print("DETAIL")
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question})

# Vote for question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay question vote form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


