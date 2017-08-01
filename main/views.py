from django.shortcuts import render


def get_index(request):
    return render(request, 'main/index.html')

def get_about(request):
    return render(request, 'main/about.html', {
        'page_title': 'Σχετικά',
    })

def get_teams(request):
    return render(request, 'main/teams.html', {
        'page_title': 'Φιλοξενούμενες Ομάδες',
    })
