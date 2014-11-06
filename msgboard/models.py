from django.db import models
from django.conf import settings

# Create your models here.
class BoardMsg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    title = models.CharField(max_length = 200)
    content = models.TextField()
    tag = models.CharField(max_length = 200)
    agreeTimes = models.IntegerField(default = 0)
    created = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

class MsgTag(models.Model):
    text = models.CharField(max_length = 200)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    

