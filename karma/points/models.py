from django.db import models
import datetime
from django.contrib.auth.models import User


class Point(models.Model):
    '''Model for Points'''
    VALUE_CHOICES = (
        (1, "+1"),
        (-1, "-1"),
    )
    created_ts = models.DateTimeField(auto_now_add=True)
    # location = models.CharField()
    comment = models.CharField(max_length=130, null=True, blank=True)
    value = models.IntegerField(choices=VALUE_CHOICES)
    cumulative_value = models.IntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.id)
    
    class Meta:
        ordering = ["-created_ts"]

    def save(self, *args, **kwargs):
        try:
            previous_point = Point.objects.filter(user=self.user).order_by('-created_ts')[0]
        except IndexError:
            self.cumulative_value = self.value
        else:
            self.cumulative_value = previous_point.cumulative_value + self.value
            
        super(Point, self).save(*args, **kwargs)