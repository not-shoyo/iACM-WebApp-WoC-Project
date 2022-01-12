from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.

def index(request):
    return render(request, "APP/index.html", {
        'numbers' : [1,2,3,4,5,6,7,8,9,10,11,12],
    })
    
def SIGpage(request, SIGname):
    return render(request, "APP/SIGpage.html", {
        'numbers' : [1,2,3,4,5,6],
        'SIGname' : SIGname.capitalize(),
    })

def sidebar(request):
    return render(request, "APP/sidebarlayout.html")