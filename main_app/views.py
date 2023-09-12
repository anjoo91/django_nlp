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
    if request.method == 'POST':
        text = request.POST.get('inputText')
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        lemmas = [token.lemma_ for token in doc]
        return render(request, 'lemma.html', {'lemmas': lemmas})
    else:
        return render(request, 'lemma.html')

def pos(request):
    nlp = spacy.load('en_core_web_sm')
    if request.method == "POST":
        pos_area = request.POST.get('pos-form')
        doc = nlp(pos_area)
        pos_list = [(token.text, token.pos_) for token in doc]
        return render(request, 'pos.html', {'pos_list': pos_list})
    else:
        return render(request, 'pos.html')

def ner(request):
    nlp = spacy.load('en_core_web_sm')
    if request.method == "POST":
        ner_area = request.POST.get('ner-form')
        doc = nlp(ner_area)
        ner_list = [(ent.text, ent.label_) for ent in doc.ents]
        return render(request, 'ner.html', {'ner_list': ner_list})
    else:
        return render(request, 'ner.html')

