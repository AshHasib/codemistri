from django.shortcuts import render

# Create your views here.

def problems(request):
    return render(request, 'problems/problems.html', {})