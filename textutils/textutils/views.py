# i have created this file- Hiba
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext=request.POST.get('text','default')
    removepunc= request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc== 'on':
        analysed= ""
        punctuations= '''!@#$%^&*()_+'"?|}{'''
        for char in djtext:
            if char not in punctuations:
                analysed= analysed + char
        params= {'purpose':'removed punctuation','analysed_text':analysed}
        djtext=analysed

    if capfirst == "on":
        analysed=""
        for char in djtext:
            analysed= analysed + char.upper()
        params = {'purpose': 'Full Caps', 'analysed_text': analysed}
        djtext=analysed

    if spaceremover == "on":
        analysed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char

        params = {'purpose': 'Space remover', 'analysed_text': analysed}
        djtext=analysed


    if newlineremover == "on":
        analysed=""
        for char in (djtext):
            if char != "\n" and char!= "\r":
              analysed = analysed + char
        params = {'purpose': 'New line remover', 'analysed_text': analysed}


    if removepunc == 'off' and capfirst == 'off' and newlineremover == 'off' and spaceremover == 'off':
        return render(request, 'error.html')

    return render(request, 'analyse.html', params)



