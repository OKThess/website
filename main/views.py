from django.shortcuts import render

from .models import Team, Job, Mentor, Meetup, Coworking


def get_index(request):
    return render(request, 'main/index.html')

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
