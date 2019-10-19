from django.shortcuts import render
from .forms import LoginForm, SignupForm
from .models import Contestant, Admin
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request, 'index.html', {})



def login(request):
    form = LoginForm()

    return render(request, 'login.html', {'form':form})



def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            f_name = data['fullName']
            u_name = data['username']
            eml = data['email']
            pro_pic = data['profile_pic']
            pwd = data['passwd']
            repwd = data['re_passwd']
            u_typ = data['user_type']

            if pwd == repwd:
                if u_typ == 'admin':
                    admin = Admin()
                    admin.fullName = f_name
                    admin.username = u_name
                    admin.email = eml
                    admin.profile_img = pro_pic
                    admin.passwd = pwd
                    admin.save()
                    return redirect('login')

                elif u_typ =='contestant':
                    contestant = Contestant()
                    contestant.fullName = f_name
                    contestant.username = u_name
                    contestant.email = eml
                    contestant.profile_img = pro_pic
                    contestant.passwd = pwd
                    contestant.save()
                    return redirect('login')
                else:
                    return HttpResponse('Please fillup properly')
            else:
                return HttpResponse('Passwords Do not match')



        return render(request, 'signup.html', {'form':form})
        

    return render(request, 'signup.html', {'form':form})




def problems(request):
    return render(request, 'problems.html', {})



def submissions(request):
    return render(request, 'submissions.html', {})




def about(request):
    return render(request, 'about.html', {})