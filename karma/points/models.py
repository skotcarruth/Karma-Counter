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
    comment = models.CharField(max_length=130, null=True, blank=True)
    value = models.IntegerField(choices=VALUE_CHOICES)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.id)
    
    class Meta:
        ordering = ["-created_ts"]
