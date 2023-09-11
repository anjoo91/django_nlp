from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
import re
import spacy


# Create your views here.
def home(request):
    return render(request, 'home.html')

def regex(request):
    if request.method =="POST":
        phonepattern=r'(\d{3})-(\d{3})-(\d{4})'
        regex_area = request.POST.get('regex-form')
        regex_phone=re.findall(phonepattern, regex_area)
        return render(request, 'regex.html', {'regex_phone': regex_phone})
    else:
        return render(request, 'regex.html')

def lemma(request):
    nlp = spacy.load('en_core_web_sm')
    if request.method =="POST":
        lemma_area = request.POST.get('lemma-form')
        doc = nlp(lemma_area)
        lemma_list = []
        for token in doc:
            lemma_list.append(token.lemma_)
        return render(request, 'lemma.html', {'lemma_list': lemma_list})
    else:
        return render(request, 'lemma.html')

def pos(request):
    return render(request, 'pos.html')

def ner(request):
    return render(request, 'ner.html')

