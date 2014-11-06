from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from msgboard import models
from msgboard import forms

# Create your views here.
def list(request, page):
    contact_list = models.BoardMsg.objects.order_by('-created')
    paginator = Paginator(contact_list, 20)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'msgboard/list.html', {
        'contacts': contacts,
        'form': forms.BoardMsgForm()
    })


@csrf_exempt
def agree(request):
    if 'id' not in request.POST:
        raise Http404
    contact = get_object_or_404(models.BoardMsg, pk = request.POST['id'])
    contact.agreeTimes += 1
    contact.save()

    return HttpResponse(contact.agreeTimes)

@login_required
def post(request):
    if request.method == 'GET':
        return render(request, 'msgboard/post.html', {
            'form': forms.BoardMsgForm(),
            'msg_tags': models.MsgTag.objects.all()
        })
    form = forms.BoardMsgForm(request.POST)
    if form.is_valid():
        c = models.BoardMsg(user = request.user,
                            title = form.cleaned_data['title'],
                            content = form.cleaned_data['content'],
                            tag = form.cleaned_data['tag'],
                            created = timezone.now())
        c.save()
        return redirect('msgboard:list', page = 1)
    else:
        return render(request, 'msgboard/post.html', {
            'form': form,
            'msg_tags': models.MsgTag.objects.all()
        })
