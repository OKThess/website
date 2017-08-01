from django.shortcuts import render


def get_index(request):
    return render(request, 'main/index.html')

def get_about(request):
    return render(request, 'main/about.html', {
        'page_title': 'Σχετικά',
    })
