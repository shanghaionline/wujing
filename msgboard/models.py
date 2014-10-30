from django.db import models
from django.conf import settings

# Create your models here.
class BoardMsg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    content = models.TextField()
    agreeTimes = models.IntegerField(default = 0)
    created = models.DateTimeField()
    

