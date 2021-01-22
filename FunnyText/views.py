#-----------My Area--------------------
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyzer(request):
    userText=request.GET.get('userText','Default')
    upperCaseYes=request.GET.get('upperCaseYes','Default')
    lowerCaseYes=request.GET.get('lowerCaseYes','Default')
    if upperCaseYes=='on':
        a=userText.upper()
    elif lowerCaseYes=='on':
        b=userText.lower()
    all_result={'upercase':a,'default':" ",'lowercase':b}
    return render(request,'index.html', all_result)