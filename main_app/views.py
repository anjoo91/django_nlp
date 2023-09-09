from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        content = render_to_string('home_content_block.html')
        return JsonResponse({'content': content})
    return render(request, 'home.html')

def regex(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        content = render_to_string('regex_content_block.html')
        return JsonResponse({'content': content})
    return render(request, 'regex.html')

def lemma(request):
    return render(request, 'lemma.html')

def pos(request):
    return render(request, 'pos.html')

def ner(request):
    return render(request, 'ner.html')

