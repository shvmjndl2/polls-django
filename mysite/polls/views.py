from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    return render(request,'polls/index.html',{'latest_question_list':latest_question_list})

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    q=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=q.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':q,'error_message':'You didnt select a choice'})
    else:
        selected_choice.votes+=1
        selected_choice.save()
    return render(request,'polls/detail.html',{'question':q})