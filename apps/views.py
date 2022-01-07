from django.shortcuts import render

# Create your views here.
from .models import Topic


def index(request):
    """"""
    return render(request, 'apps/index.html')


def topics(request):
    """"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'apps/topics.html', context)

def topic(request, topic_id):
    """"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'apps/topic.html', context)


from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm


def new_topic(request):

    if request.method != 'POST':

        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('apps:topics'))

    context = {'form': form}
    return render(request, 'apps/new_topic.html', context)