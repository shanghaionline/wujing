from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class ChatUserManager(models.Manager):
    def get_channel(self, name):
        try:
            user = User.objects.get(username = name)
        except User.DoesNotExist:
            return None
        return self.get_user(user)

    def get_user(self, user, id = 0):
        now = timezone.now();
        if not user.is_authenticated():
            user = None
            name = '匿名'
            query = self.filter(id = id, user = None)
        else:
            name = user.username
            query = self.filter(user = user)
        query = query.filter(user_type = ChatUser.CHATUSER)
        try:
            data = query.get()
        except ChatUser.DoesNotExist:
            data = ChatUser(name = name, user_type = ChatUser.CHATUSER,
                            user = user, created = now, last_access = now)
            data.save()
        return data

class MessageManager(models.Manager):
    def push_message(self, user, target, message):
        now = timezone.now()
        data = Message(target = target, source = user, message = message,
                       created = now)
        data.save()
        return data

    def poll_message(self, user, target):
        dialogue = Dialogue.objects.get_dialogue(user, target)
        query = self.exclude(source = user).filter(target = user,
                            created__gt = dialogue.last_access)
        if target is not None:
            query = query.filter(source = target)
        query = query.order_by('created')
        if query.last():
            dialogue.last_access = query.last().created
            dialogue.save()
        return query

class DialogueManager(models.Manager):
    def join_user(self, user, target):
        if not (user.id == target.id or 
                target.user_type == ChatUser.CHANNEL and user.user is not None and user.user.is_staff):
            return None
        try:
            data = self.get(owner = user, target = target)
        except Dialogue.DoesNotExist:
            now = timezone.now()
            data = Dialogue(owner = user, target = target, right = 'R', last_access = now)
            data.save()
        return data

    def get_dialogue(self, user, target):
        try:
            dialogue = Dialogue.objects.get(owner = user, target = target)
            print('============================================')
        except Dialogue.DoesNotExist:
            dialogue = Dialogue(owner = user, target = target, right = 'R',
                                last_access = datetime.datetime.fromtimestamp(0))
            print('++++++++++++++++++++++++++++++++++++++++++++')
            dialogue.save()
        return dialogue
        

# Create your models here.
class ChatUser(models.Model):
    UNKNOWN = 0
    CHATUSER = 1
    CHANNEL = 2
    USER_TYPE_CHOICES = (
        (UNKNOWN, '未知'), (CHATUSER, '用户'), (CHANNEL, '频道'),)

    name = models.CharField(max_length = 100)
    user_type = models.IntegerField(choices = USER_TYPE_CHOICES, default=UNKNOWN)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, related_name='+')
    created = models.DateTimeField()
    last_access = models.DateTimeField()

    objects = ChatUserManager()
    
class Message(models.Model):
    target = models.ForeignKey(ChatUser)
    source = models.ForeignKey(ChatUser, related_name='+')
    message = models.TextField()
    created = models.DateTimeField()

    objects = MessageManager()

class Dialogue(models.Model):
    owner = models.ForeignKey(ChatUser)
    target = models.ForeignKey(ChatUser, null = True, related_name='+')
    right = models.CharField(max_length = 80)
    last_access = models.DateTimeField()

    objects = DialogueManager()
