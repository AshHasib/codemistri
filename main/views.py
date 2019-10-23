from django.shortcuts import render
from .forms import LoginForm, SignupForm
from .models import Profile
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    if request.GET.get('Logout') == 'Logout':
        request.session.flush()
        return redirect('login')

    if request.session.has_key('username'):
        user = None

        try:
            user = Profile.objects.get(username = request.session.get('username'))
            data_dict = {
                'username':user.username
            }
            return render(request, 'index.html', data_dict)

        except Exception as e:
            print(e)
            return redirect('login')

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

            try:
                user = Profile.objects.get(username = u_name, password= passwd, user_type = u_typ)
                request.session['username'] = user.username
                request.session['user_type'] = user.user_type
                return redirect('index')

            except ObjectDoesNotExist as e:
                print(e)
                return HttpResponse('Invalid username or password')

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
                user = Profile()
                user.fullName = f_name
                user.username = u_name
                user.email = eml
                user.profile_img = pro_pic
                user.password = pwd
                user.user_type = u_typ
                user.save()
                return redirect('login')
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