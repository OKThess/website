from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import Team, Mentor, Meetup, Coworking, Post, Event
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

def program_redir(request):
    return redirect(reverse('main:program_teams'))

def get_program_teams(request):
    teams = Team.objects.filter(alumni=False).order_by('name')
    return render(request, 'main/program-teams.html', {
        'teams': teams,
    })

def get_program_mentors(request):
    mentors = Mentor.objects.order_by('name')
    return render(request, 'main/program-mentors.html', {
        'mentors': mentors,
    })

def get_program_alumni(request):
    teams = Team.objects.filter(alumni=False).order_by('name')
    return render(request, 'main/program-alumni.html', {
        'teams': teams,
    })

def get_events(request):
    return render(request, 'main/events.html')

def get_blog(request):
    return render(request, 'main/blog.html')

def get_blog_post_sample(request):
    return render(request, 'main/post.html')

def get_contact(request):
    return render(request, 'main/contact.html')

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

def health(request):
    return HttpResponse('Ok')
