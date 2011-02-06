import json
from django.contrib.auth.models import User
from karma.points.models import Point
from django.http import HttpResponse


def users(request):
    users = User.objects.all()
    return HttpResponse(json.dumps(
        map(lambda user: {
            'id': user.id, 
            'username': user.username,
        }, users)
    ), mimetype="text/plain")    

def userkarma(request, user_id=None):
    user = User.objects.get(pk=user_id)
    return HttpResponse(json.dumps({
        'id': user.id,
        'username': user.username,
        'points': map(lambda point: {
            'created_ts': str(point.created_ts),
            'value': point.value,
        }, user.point_set.all()),
    }), mimetype="text/plain")

def add(request, user_id=None, value=None):
    user = User.objects.get(pk=user_id)
    point = Point(
        user=user,
        value=(1 if value == 'up' else -1),
    )
    point.save()
    return HttpResponse(json.dumps({
        'created_ts': str(point.created_ts),
        'value': point.value,
    }), mimetype="text/plan")
