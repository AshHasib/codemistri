from .models import Profile
from django.shortcuts import redirect
def getCurrentUser(request):
    usr = None

    try:
        usr = Profile.objects.get(username = request.session.get('username'))
        return {'currentUser':usr.username}

    except Exception as e:
        print(e)
        return {'currentUser':'None'}


def test_processor(request):
    print('Test processor is called . . .')
    return {'logout': 'Logout User'}