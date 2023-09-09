from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'home.html')

def regex(request):
    print("Inside regex view")  # Debugging line
    return render(request, 'regex.html')

def lemma(request):
    return render(request, 'lemma.html')

def pos(request):
    return render(request, 'pos.html')

def ner(request):
    return render(request, 'ner.html')

