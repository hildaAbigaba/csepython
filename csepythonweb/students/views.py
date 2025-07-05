from django.shortcuts import render

# Create your views here.

def studentspage(request):
    return render(request, "students.html")

def studentleadershippage(request):
    return render(request, "studentleader.html")
