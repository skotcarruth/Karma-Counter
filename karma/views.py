from django.shortcuts import render_to_response
from karma.points.models import Point
from django.contrib.auth.models import User

def index(request):
    '''homepage view'''
    points = Point.objects.all()
    return render_to_response('index.html', {
        'points': points,
    })

def dashboard(request, user_id=None):
    '''user dashboard page'''
    user = User.objects.get(pk=user_id)
    points = user.point_set.all()
    return render_to_response('dashboard.html', {
        'points': points,
        'user': user,
    })