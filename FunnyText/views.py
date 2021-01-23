#-----------My Area--------------------
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyzer(request):

    userText=request.POST.get('userText','default')
    print(userText)
    upperCaseYes=request.POST.get('upperCaseYes','off')
    print(upperCaseYes)
    lowerCaseYes=request.POST.get('lowerCaseYes','off')
    print(lowerCaseYes)
    removepunc=request.POST.get('removepunc','off')
    if upperCaseYes=='on':
        abc=''
        for char in userText:
            abc=abc+char.upper()
        param={'convert':abc}
        userText=abc
    elif lowerCaseYes=='on':
        abc=''
        for char in userText:
            abc=abc+char.lower()
        param={'convert':abc}
        userText=abc
    if removepunc == "on":
        punctuations = '''!()-[]{};:'" \,<>./?@#$%^&*_~'''
        abc = ""
        for char in userText:
            if char not in punctuations:
                abc= abc + char
        param={'convert':abc}
        userText=abc
    return render(request,'index.html',param)