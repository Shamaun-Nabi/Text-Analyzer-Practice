#-----------My Area--------------------
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def sumCal(request):
    firstNumber=request.GET.get('firstNumber','0')
    secondNumber=request.GET.get('secondNumber','0')
    add=int(firstNumber)+int(secondNumber)
    my_result={"ans":add}
    
    return render(request,'index.html',my_result)