from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def problems(request):
    if request.GET.get('Logout') == 'Logout':
        request.session.flush()
        return redirect('login')


    return render(request, 'problems/problems.html', {})