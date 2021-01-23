#-----------My Area--------------------
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyzer(request):
    userText=request.GET.get('userText','default')
    print(userText)
    upperCaseYes=request.GET.get('upperCaseYes','off')
    print(upperCaseYes)
    lowerCaseYes=request.GET.get('lowerCaseYes','off')
    print(lowerCaseYes)
    if upperCaseYes=='on':
        abc=''
        for char in userText:
            abc=abc+char.upper()
        param={'convert':abc}
        userText=abc
    if lowerCaseYes=='on':
        abc=''
        for char in userText:
            abc=abc+char.lower()
        param={'convert':abc}
        userText=abc
    
    
    return render(request,'index.html',param)