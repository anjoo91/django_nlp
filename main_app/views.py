from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def regex(request):
    return render(request, 'regex.html')

def lemma(request):
    return render(request, 'lemma.html')

def pos(request):
    return render(request, 'pos.html')

def ner(request):
    return render(request, 'ner.html')

