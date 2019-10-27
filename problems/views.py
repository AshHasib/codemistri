from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProblemForm
# Create your views here.

def problems(request):
    if request.GET.get('Logout') == 'Logout':
        request.session.flush()
        return redirect('login')



    return render(request, 'problems/problems.html', {})


def problemList(request, category):
    print('INSIDE PROBLEM LIST VIEW')
    # getting the problems by category

    # Create problem button


    return render(request, 'problems/problem_list.html', {})



def create(request):
    print('INSIDE CREATE PROBLEM VIEW')

    form = ProblemForm()

    if request.method =='POST':
        form = ProblemForm(request.POST)

    return render(request, 'problems/create_problem.html',{'form':form})