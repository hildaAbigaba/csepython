from django.shortcuts import render

# Create your views here.

def programspage(request):
    return render(request, "programs.html")
