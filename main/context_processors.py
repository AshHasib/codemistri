from .models import Profile

def getCurrentUser(request):
    usr = None

    try:
        usr = Profile.objects.get(username = request.session.get('username'))
        return {'currentUser':usr.username}

    except Exception as e:
        print(e)
        return {'currentUser':'None'}