import json
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, HttpResponse
from chatroom import models
from chatroom import forms
# Create your views here.

def go_room(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        raise Http404
    if request.user.is_authenticated():
        return redirect('chatroom:room', name = name)
    chatroom_url = reverse('chatroom:room', args=(name,))
    return render(request, 'chatroom/go-room.html' , 
                  {'chatroom_name':name, 'chatroom_url':chatroom_url})

def room(request, name):
    user = models.ChatUser.objects.get_user(request.user, 
                                            request.session.get('chat_user_id', 0))
    request.session['chat_user_id'] = user.id
    data = {'chat_user': user}
    if name is not None:
        target = models.ChatUser.objects.get_channel(name)
    else:
        target = None
    if target is not None:
        data['chat_target'] = target
    return render(request, 'chatroom/room.html', data)


@user_passes_test(lambda user:user.is_staff)
def room_admin(request):
    return room(request, None)

def push(request):
    form = forms.PushMessageForm(request.POST)
    user = models.ChatUser.objects.get_user(request.user, 
                                            request.session.get('chat_user_id', 0))
    request.session['chat_user_id'] = user.id
    if not form.is_valid():
        return HttpResponse(json.dumps({'error':form.errors}))
    try:
        target = models.ChatUser.objects.get(pk = form.cleaned_data['target'])
    except models.ChatUser.DoesNotExist:
        raise Http404
    msg = models.Message.objects.push_message(user, target, form.cleaned_data['message'])
    data = {'id': msg.id, 'target': msg.target.id, 'source': msg.source.id,
            'name': chat_user_name(msg.source), 'receiver': chat_user_name(msg.target), 'message':msg.message}
    return HttpResponse(json.dumps(data))

def chat_user_name(user):
    if user.user is None:
        name = '%s%d' % (user.name, user.id)
    else:
        name = user.user.username
    return name

def poll(request):
    user = models.ChatUser.objects.get_user(request.user, 
                                            request.session.get('chat_user_id', 0))
    request.session['chat_user_id'] = user.id
    if 'id' in request.POST:
        try:
            target = models.ChatUser.objects.get(pk = request.POST['id'])
        except models.ChatUser.DoesNotExist:
            raise Http404
    else:
        target = None
    message_list = models.Message.objects.poll_message(user, target)
    data = []
    for item in message_list:
        msg = {'id': item.id, 'target': item.target.id, 'source': item.source.id,
               'name': chat_user_name(item.source), 'receiver': chat_user_name(item.target), 'message':item.message}
        data.append(msg)
    return HttpResponse(json.dumps({'name': chat_user_name(user), 'data':data}))

            
