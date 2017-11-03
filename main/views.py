import datetime, itertools

from collections import OrderedDict

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string

from okthess import settings
from .models import Team, Mentor, Meetup, Coworking, Post, Event, About, OkthessMeetup, ResourceCategory, Resource, ApplyText, Partner
from .forms import ApplicationForm, ContactForm


def index(request):
    if request.LANGUAGE_CODE == 'en':
        featured_posts_list = Post.en_objects.filter(is_featured=True)
        for post in featured_posts_list:
            post.title = post.title_en
            post.teaser = post.teaser_en
            post.body = post.body_en
    else:
        featured_posts_list = Post.el_objects.filter(is_featured=True)
        for post in featured_posts_list:
            post.title = post.title_el
            post.teaser = post.teaser_el
            post.body = post.body_el
    events_list = Event.objects.order_by('-date').filter(date__gte=datetime.datetime.now())[:3]
    return render(request, 'main/index.html', {
        'featured_posts_list': featured_posts_list,
        'events_list': events_list,
    })


def about(request):
    about_texts = About.objects.first()
    if request.LANGUAGE_CODE == 'en':
        partners_list = Partner.en_objects.order_by('name')
        for partner in partners_list:
            partner.description = partner.description_en
        if about_texts:
            about_texts.what_text = about_texts.what_text_en
            about_texts.how_text = about_texts.how_text_en
            about_texts.participate_text = about_texts.participate_text_en
            about_texts.coworking_text = about_texts.coworking_text_en
    else:
        partners_list = Partner.el_objects.order_by('name')
        for partner in partners_list:
            partner.description = partner.description_el
        if about_texts:
            about_texts.what_text = about_texts.what_text_el
            about_texts.how_text = about_texts.how_text_el
            about_texts.participate_text = about_texts.participate_text_el
            about_texts.coworking_text = about_texts.coworking_text_el
    return render(request, 'main/about.html', {
        'about_texts': about_texts,
        'partners_list': partners_list,
    })


def program_redir(request):
    return redirect(reverse('main:program_teams'))


def program_teams(request):
    if request.LANGUAGE_CODE == 'en':
        teams_list = Team.en_objects.filter(alumni=False).order_by('name')
        for team in teams_list:
            team.description = team.description_en
    else:
        teams_list = Team.el_objects.filter(alumni=False).order_by('name')
        for team in teams_list:
            team.description = team.description_el
    return render(request, 'main/program-teams.html', {
        'teams_list': teams_list,
    })


def program_mentors(request):
    if request.LANGUAGE_CODE == 'en':
        mentors_list = Mentor.en_objects.order_by('name')
        for mentor in mentors_list:
            mentor.description = mentor.description_en
    else:
        mentors_list = Mentor.el_objects.order_by('name')
        for mentor in mentors_list:
            mentor.description = mentor.description_el
    return render(request, 'main/program-mentors.html', {
        'mentors_list': mentors_list,
    })


def program_partners(request):
    if request.LANGUAGE_CODE == 'en':
        partners_list = Partner.en_objects.order_by('name')
        for partner in partners_list:
            partner.description = partner.description_en
    else:
        partners_list = Partner.el_objects.order_by('name')
        for partner in partners_list:
            partner.description = partner.description_el
    return render(request, 'main/program-partners.html', {
        'partners_list': partners_list,
    })


def program_alumni(request):
    if request.LANGUAGE_CODE == 'en':
        teams_list = Team.en_objects.filter(alumni=True).order_by('name')
        for team in teams_list:
            team.description = team.description_el
    else:
        teams_list = Team.el_objects.filter(alumni=True).order_by('name')
        for team in teams_list:
            team.description = team.description_el
    return render(request, 'main/program-alumni.html', {
        'teams_list': teams_list,
    })


def meetup(request):
    latest_meetup = OkthessMeetup.objects.order_by('-date').first()
    return render(request, 'main/meetup.html', {
        'latest_meetup': latest_meetup,
    })


def events(request):
    events_list_all = Event.objects.order_by('-date')
    events_archive = {}
    for event in events_list_all:
        if event.date.year not in events_archive:
            events_archive[event.date.year] = {}
        if event.date.month >= 1 and event.date.month <= 3:
            events_archive[event.date.year].setdefault('Jan-Feb-Mar', []).append(event)
        elif event.date.month >= 4 and event.date.month <= 6:
            events_archive[event.date.year].setdefault('Apr-May-Jun', []).append(event)
        elif event.date.month >= 7 and event.date.month <= 9:
            events_archive[event.date.year].setdefault('Jul-Aug-Sep', []).append(event)
        elif event.date.month >= 10 and event.date.month <= 12:
            events_archive[event.date.year].setdefault('Oct-Nov-Dev', []).append(event)
    events_archive = OrderedDict(reversed(sorted(events_archive.items())))
    now = datetime.datetime.now()
    future_events_number = 0
    for event in events_list_all:
        if datetime.datetime.combine(event.date, datetime.time(0, 0)) > now:
            future_events_number += 1
    events_list_future = reversed(Event.objects.order_by('-date')[:future_events_number])
    events_list_past = Event.objects.order_by('-date')[future_events_number:10]
    events_list = itertools.chain(events_list_future, events_list_past)
    meetups = Meetup.objects.order_by('name')
    return render(request, 'main/events.html', {
        'events_archive': events_archive,
        'events_list': events_list,
        'meetups': meetups,
    })


def blog(request):
    if request.LANGUAGE_CODE == 'en':
        posts_list = Post.en_objects.order_by('-date')[:10]
        for post in posts_list:
            post.title = post.title_en
            post.teaser = post.teaser_en
            post.body = post.body_en
    else:
        posts_list = Post.el_objects.order_by('-date')[:10]
        for post in posts_list:
            post.title = post.title_el
            post.teaser = post.teaser_el
            post.body = post.body_el
    if request.LANGUAGE_CODE == 'en':
        posts_list_all = Post.en_objects.all()
        for post in posts_list_all:
            post.title = post.title_en
            post.teaser = post.teaser_en
            post.body = post.body_en
    else:
        posts_list_all = Post.el_objects.all()
        for post in posts_list_all:
            post.title = post.title_el
            post.teaser = post.teaser_el
            post.body = post.body_el
    archives_list = []
    for post in posts_list_all:
        post_date = post.date.replace(day=1)
        if not post_date in archives_list:
            archives_list.append(post_date)
    resources_list = Resource.objects.filter(is_pinned=True)
    return render(request, 'main/blog.html', {
        'posts_list': posts_list,
        'archives_list': archives_list,
        'resources_list': resources_list,
    })


def blog_post(request, post_slug):
    if request.LANGUAGE_CODE == 'en':
        post = Post.en_objects.get(slug=post_slug)
        post.title = post.title_en
        post.teaser = post.teaser_en
        post.body = post.body_en
    else:
        post = Post.el_objects.get(slug=post_slug)
        post.title = post.title_el
        post.teaser = post.teaser_el
        post.body = post.body_el
    return render(request, 'main/post.html', {
        'post': post,
    })


def blog_archives(request, archive_year, archive_month):
    if request.LANGUAGE_CODE == 'en':
        posts_list = Post.en_objects.filter(date__year=archive_year, date__month=archive_month)
        for post in posts_list:
            post.title = post.title_en
            post.teaser = post.teaser_en
            post.body = post.body_en
    else:
        posts_list = Post.el_objects.filter(date__year=archive_year, date__month=archive_month)
        for post in posts_list:
            post.title = post.title_el
            post.teaser = post.teaser_el
            post.body = post.body_el
    posts_list_all = Post.objects.all()
    archives_list = []
    for post in posts_list_all:
        post_date = post.date.replace(day=1)
        if not post_date in archives_list:
            archives_list.append(post_date)
    return render(request, 'main/blog-archive.html', {
        'posts_list': posts_list,
        'archives_list': archives_list,
        'archive_year': archive_year,
    })


def resources(request):
    categories_list = ResourceCategory.objects.all()
    return render(request, 'main/resources.html', {
        'categories_list': categories_list,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            content_vars = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            send_mail(
                'Contact form submission from okthess.gr',
                render_to_string('main/contact-email.txt', content_vars),
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_TO_EMAIL],
            )
            messages.info(request, "Thank you for contacting us! We'll answer ASAP.")
            return HttpResponseRedirect(reverse('main:contact'))
        else:
            return HttpResponse('Contact form is invalid.')
    else:
        return render(request, 'main/contact.html')


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for applying!')
            return HttpResponseRedirect(reverse('main:apply'))
        else:
            return HttpResponse('Application form submission is invalid.')
    else:
        form = ApplicationForm()
        apply_text = ApplyText.objects.first()
        application_content = ''
        if apply_text:
            if request.LANGUAGE_CODE == 'en':
                application_content = apply_text.content_en
            else:
                application_content = apply_text.content_el
        return render(request, 'main/apply.html', {
            'form': form,
            'application_content': application_content,
        })
