from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Invitation


def index(request):
    return HttpResponseRedirect('/')


def detail(request, invitation_id):
    try:
        invitation = Invitation.objects.get(pk=invitation_id)
    except Invitation.DoesNotExist:
        raise Http404("Invitation does not exist")
    return render(request, 'invitation/index.html', {'invitation': invitation})


def confirm(request, invitation_id):
    try:
        invitation = Invitation.objects.get(pk=invitation_id)
    except Invitation.DoesNotExist:
        raise Http404("Invitation does not exist")

    value = request.POST['number_n']
    invitation.n_people_confirm = value

    invitation.status = True
    invitation.not_coming = False
    if int(value) == 0:
        invitation.not_coming = True
        invitation.status = False

    invitation.save()
    return HttpResponseRedirect(reverse('invitation:detail', args=(invitation.id,)))


def notComing(request, invitation_id):
    try:
        invitation = Invitation.objects.get(pk=invitation_id)
    except Invitation.DoesNotExist:
        raise Http404("Invitation does not exist")

    invitation.status = False
    invitation.not_coming = True
    invitation.n_people_confirm = 0

    invitation.save()
    return HttpResponseRedirect(reverse('invitation:detail', args=(invitation.id,)))


def page_not_found_view(request, exception):
    return render(request, '404.html')


def server_error_view(request):
    return render(request, '500.html')
