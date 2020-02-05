from django.shortcuts import render

def homepage(request):
    return render(request,'last_one/homepage.html')
