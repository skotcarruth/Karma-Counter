from points.models import Point
from django.contrib import admin

class PointAdmin(admin.ModelAdmin):
   list_display = ('user', 'value', 'comment', 'created_ts')

admin.site.register(Point, PointAdmin)
