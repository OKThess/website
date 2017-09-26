from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import Team, Mentor, Meetup, Coworking, Post, Event
from .forms import ApplicationForm


def index(request):
    featured_posts = Post.objects.filter(is_featured=True)
    events_list = Event.objects.order_by('-date')[:3]
    return render(request, 'main/index.html', {
        'featured_posts': featured_posts,
        'events_list': events_list,
    })


def about(request):
    return render(request, 'main/about.html', {
        'page_title': 'Σχετικά',
    })


def program_redir(request):
    return redirect(reverse('main:program_teams'))


def program_teams(request):
    teams_list = Team.objects.filter(alumni=False).order_by('name')
    for team in teams_list:
        if request.LANGUAGE_CODE == 'el':
            team.description = team.description_el
    return render(request, 'main/program-teams.html', {
        'teams_list': teams_list,
    })


def program_mentors(request):
    mentors_list = Mentor.objects.order_by('name')
    for mentor in mentors_list:
        if request.LANGUAGE_CODE == 'el':
            mentor.description = mentor.description_el
    return render(request, 'main/program-mentors.html', {
        'mentors_list': mentors_list,
    })


def program_alumni(request):
    teams = Team.objects.filter(alumni=True).order_by('name')
    return render(request, 'main/program-alumni.html', {
        'teams': teams,
    })


def program_meetup(request):
    return render(request, 'main/program-meetup.html')


def events(request):
    events = Event.objects.order_by('-date')[:10]
    meetups = Meetup.objects.order_by('name')
    return render(request, 'main/events.html', {
        'events': events,
        'meetups': meetups,
    })


def blog(request):
    posts_list = Post.objects.order_by('-date')[:10]
    for post in posts_list:
        if request.LANGUAGE_CODE == 'el':
            post.title = post.title_el
            post.teaser = post.teaser_el
    posts_list_all = Post.objects.all()
    archives_list = []
    for post in posts_list_all:
        post_date = post.date.replace(day=1)
        if not post_date in archives_list:
            archives_list.append(post_date)
    return render(request, 'main/blog.html', {
        'posts_list': posts_list,
        'archives_list': archives_list,
    })


def blog_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    if request.LANGUAGE_CODE == 'el':
        post.title = post.title_el
        post.body = post.body_el
    return render(request, 'main/post.html', {
        'post': post,
    })


def blog_archives(request, archive_year, archive_month):
    posts_list = Post.objects.filter(date__year=archive_year, date__month=archive_month)
    for post in posts_list:
        if request.LANGUAGE_CODE == 'el':
            post.title = post.title_el
            post.teaser = post.teaser_el
    posts_list_all = Post.objects.all()
    archives_list = []
    for post in posts_list_all:
        post_date = post.date.replace(day=1)
        if not post_date in archives_list:
            archives_list.append(post_date)
    return render(request, 'main/blog-archive.html', {
        'posts_list': posts_list,
        'archives_list': archives_list,
    })


def contact(request):
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
        return render(request, 'main/apply.html', {
            'form': form,
        })
