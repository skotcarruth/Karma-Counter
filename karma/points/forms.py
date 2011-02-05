from django import forms
from karma.points.models import Point


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ('value', 'comment',)