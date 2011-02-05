from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from karma.points.models import Point
from karma.points import forms


def index(request):
    '''homepage view'''
    points = Point.objects.all()
    return render_to_response('index.html', {
        'points': points,
    })
    
def add(request):
    '''add point page'''
    if request.method == 'POST':
        form = forms.PointForm(request.POST)
        if form.is_valid():
            point = form.save(commit=False)
            point.user = request.user
            point.save()
            return HttpResponseRedirect(reverse('points.views.index'))
    else:
        form = forms.PointForm()
        
    return render_to_response('points/add.html', {
        'form': form,
    }, 
    RequestContext(request)
    )