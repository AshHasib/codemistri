from .models import Profile
from django.shortcuts import redirect

def getCurrentUser(request):
    usr = None

    try:
        usr = Profile.objects.get(username = request.session.get('username'))
        return {'username':usr.username, 'isAdmin':usr.isAdmin()}

    except Exception as e:
        print(e)
        return {'currentUser':'None'}
