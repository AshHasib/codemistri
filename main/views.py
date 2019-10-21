from django.shortcuts import render
from .forms import LoginForm, SignupForm
from .models import Contestant, Admin
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def index(request):

    if request.session.has_key('username'):
        user = None
        if request.session.get('user_type') == 'contestant':
            user = Contestant.objects.get(username = request.session.get('username'))

        elif request.session.get('user_type') == 'admin':
            user = Admin.objects.get(username = request.session.get('username'))

        data_dict = {
            'username':user.username
        }
        return render(request, 'index.html', data_dict)


    else:
        return redirect('login')



def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if(form.is_valid()):
            data  = form.cleaned_data

            u_name = data['username']
            passwd = data['password']
            u_typ = data['user_type']

            if u_typ == 'contestant':
                try:
                    contestant = Contestant.objects.get(username = u_name)
                    # print('USer - {}'.format(contestant))

                    request.session['username']=contestant.username
                    request.session['user_type']=u_typ
                    return redirect('index')

                except Exception as e:
                    print(e)

            elif u_typ == 'admin':
                try:
                    admin = Admin.objects.get(username = u_name)
                    print('Admin found - {}'.format(admin))

                    request.session['username']=admin.usename
                    request.session['user_type']=u_typ
                    return redirect('index')
                except Exception as e:
                    print(e)

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