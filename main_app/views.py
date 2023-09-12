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
        regex_area = request.POST['regex-form']
        print("Debug:", regex_area)
        regex_phone=re.findall(phonepattern, regex_area)
        print(regex_phone)
        return render(request, 'regex.html', {'regex_phone': regex_phone})
    else:
        return render(request, 'regex.html')

def lemma(request):
    nlp = spacy.load('en_core_web_sm')
    if request.method == 'POST':
        lemma_area = request.POST['lemma-form']
        lemma_area = nlp(lemma_area)
        print("Inside POST block")
        print("Lemma Area:", lemma_area)
        token_list = [i.text for i in lemma_area]
        tokens=[i for i in token_list]
        print(tokens)
        lemmas_list = [i.lemma_ for i in lemma_area]
        lemmas=[i for i in lemmas_list]
        print(lemmas)
        zipped_words = zip(tokens, lemmas)
        return render(request, 'lemma.html', {'zipped_words': zipped_words})
    else:
        return render(request, 'lemma.html')

def pos(request):
    nlp = spacy.load('en_core_web_sm')
    if request.method == "POST":
        pos_area = request.POST['pos-form']
        pos_area = nlp(pos_area)
        pos_tokens_list = [i.text for i in pos_area]
        pos_tokens=[i for i in pos_tokens_list]
        pos_results_list=[i.pos_ for i in pos_area]    
        pos_results = [i for i in pos_results_list] 
        explain_pos_list=[spacy.explain(i) for i in pos_results]  
        explain_individual_pos=[i for i in explain_pos_list]
        zipped_pos = zip(pos_tokens, pos_results, explain_individual_pos)
        return render(request, 'pos.html', {'zipped_pos': zipped_pos})
    else:
        return render(request, 'pos.html')

def ner(request):
    nlp = spacy.load('en_core_web_sm')
    if request.method == "POST":
        ner_area = request.POST['ner-form']
        ner_area = nlp(ner_area)
        ner_tokenslabels_list = [(i.text, i.label_) for i in ner_area.ents]
        ner_tokenslabels = [i for i in ner_tokenslabels_list]
        onlylabels = [i.label_ for i in ner_area.ents]
        ner_explain_list = [spacy.explain(i) for i in onlylabels]
        ner_explain_individual=[i for i in ner_explain_list]
        zipped_ner = zip((entity for entity, label in ner_tokenslabels), 
                     (label for entity, label in ner_tokenslabels), 
                     ner_explain_individual)
        return render(request, 'ner.html', {'zipped_ner': zipped_ner})
    else:
        return render(request, 'ner.html')

