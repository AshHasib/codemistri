from django import forms
USER_TYPE = [('contestant','Contestant'),('admin','Administrator')]

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget = forms.TextInput(
        attrs = {
            'placeholder':'Enter username (e.g. johndoe)'
        }
    ))
    password = forms.CharField(label='',widget = forms.PasswordInput(
        attrs = {
            'placeholder':'Enter password (max length 20)'
        }
    ))
    user_type =  forms.CharField(label='I am a ', widget=forms.Select(choices=USER_TYPE))



class SignupForm(forms.Form):
    fullName = forms.CharField(label='Full Name', widget = forms.TextInput(attrs= {'placeholder':'Enter Full Name'}))
    username = forms.CharField(label='Username', widget = forms.TextInput(attrs= {'placeholder':'Enter Username'}))
    email = forms.EmailField(label='Email', widget = forms.TextInput(attrs= {'placeholder':'Enter Email'}))
    profile_pic = forms.ImageField(label='Profile Image')
    passwd = forms.CharField(label='Enter Password', widget= forms.PasswordInput(attrs={'placeholder':'Password'}))
    re_passwd = forms.CharField(label='Retype Password', widget= forms.PasswordInput(attrs={'placeholder':'Retype Password'}))
    user_type = forms.CharField(label = 'I want myself as',  widget=forms.Select(choices=USER_TYPE))
