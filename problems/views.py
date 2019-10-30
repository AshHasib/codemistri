from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreateProblemForm
from .models import Problem
from main.models import Profile
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

'''
fields - 
title, description, constraint, input_desc, output_desc, sample_input, sample_output, category
'''

def create(request):
    print('INSIDE CREATE PROBLEM VIEW')
    try:
        user = Profile.objects.get(username = request.session.get('username'))
        form = CreateProblemForm(request.POST or None)
        #print('Try catch initial block succss..')
        #print(user)
        if form.is_valid():
            data = form.cleaned_data
            problem = Problem.objects.createProblem(
                setter= user,
                title = data['title'],
                description= data['description'],
                constraint = data['constraint'],
                input_desc= data['input_desc'],
                output_desc= data['output_desc'],
                sample_input= data['sample_input'],
                sample_output= data['sample_output'],
                category= data['category'],
                difficulty=data['difficulty']
            )
            
            try:
                problem.save()
                print('Problem saved successfully')
                return redirect('problems')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

    return render(request, 'problems/create_problem.html',{'form':form})