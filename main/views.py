from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Team, Job, Mentor, Meetup, Coworking, Post, Event
from .forms import ApplicationForm


def get_index(request):
    featured_posts = Post.objects.filter(is_featured=True)
    events = Event.objects.all()
    return render(request, 'main/index.html', {
        'featured_posts': featured_posts,
        'events': events,
    })

def get_about(request):
    return render(request, 'main/about.html', {
        'page_title': 'Σχετικά',
    })

def get_teams(request):
    teams = Team.objects.order_by('name')
    jobs = Job.objects.all()
    mentors = Mentor.objects.all()
    coworkings = Coworking.objects.all()
    meetups = Meetup.objects.all()
    return render(request, 'main/teams.html', {
        'page_title': 'Φιλοξενούμενες Ομάδες',
        'teams': teams,
        'jobs': jobs,
        'mentors': mentors,
        'meetups': meetups,
        'coworkings': coworkings,
    })

def get_news(request):
    posts = Post.objects.all()
    return render(request, 'main/news.html', {
        'posts': posts,
    })

def get_news_single(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'main/post.html', {
        'post': post,
    })

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for applying!')
            return HttpResponseRedirect('/apply')
        else:
            return HttpResponse('Application form submission is invalid.')
    else:
        form = ApplicationForm()
        return render(request, 'main/apply.html', {'form': form})

def contact(request):
    return HttpResponseRedirect('/')
