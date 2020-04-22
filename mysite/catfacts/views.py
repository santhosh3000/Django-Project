from django.shortcuts import render
from django.http import HttpResponse
import requests
from catfacts.models import CatFact


#/catfacts/random-fact
def random(request):
    req = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat')
    fact = req.json()
    text = fact['text']
    model_fact = CatFact(fact=text)
    model_fact.save()
    return HttpResponse('<p>{}</p>'.format(text))


#/catfacts/latest-facts
def viewall(request):
    html = '<p>'
    for index, fact in enumerate(CatFact.objects.order_by('-id')[:5]): #shows the lastest five facts that was shown in /catfacts
            html += "{}.) ".format(index + 1)
            html += str(fact)
            html += '<br/>'
    html += '</p>'
    return HttpResponse(html)

