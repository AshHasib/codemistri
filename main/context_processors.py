from .models import Contestant, Admin

def getCurrentUser(request):
    usr = None
    if request.session.get('user_type') == 'contestant':
        usr = Contestant.objects.get(username = request.session.get('username'))
    else:
        usr = Admin.objects.get(username = request.session.get('username'))
    return {'currentUser':usr.username}
