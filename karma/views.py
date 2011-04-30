from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from karma.points.models import Point
from django.db.models import Sum


def index(request):
    '''homepage view'''
    points = Point.objects.all()
    create_user_form = UserCreationForm()
    login_form = AuthenticationForm()
    return render_to_response('index.html', {
        'points': points[:20],
        'create_user_form': create_user_form,
        'login_form': login_form,
        'is_logged_in': request.user.is_authenticated(),
    }, RequestContext(request))

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('karma.points.views.add'))
        else:
            # Return a 'disabled account' error message
            return HttpResponseRedirect(reverse('karma.views.index'))
      else:
         # Return an 'invalid login' error message.
         return HttpResponseRedirect(reverse('karma.views.index'))
   else:
      return HttpResponseRedirect(reverse('karma.views.index'))


def logout(request):
   auth_logout(request)
   return HttpResponseRedirect(reverse('karma.views.index'))

def register(request):
   pass

def userkarma(request, user_id=None):
    '''user karma page'''
    user = User.objects.get(pk=user_id)
    points = user.point_set.all()
    total_points = user.point_set.all().aggregate(Sum('value'))['value__sum']
    return render_to_response('users/userkarma.html', {
        'points': points,
        'user': user,
        'total_points': total_points,
    }, RequestContext(request))
    
def userindex(request):
    '''user index page'''
    users = User.objects.all()
    return render_to_response('users/index.html', {
        'users': users,
    }, RequestContext(request))
