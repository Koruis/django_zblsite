from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    login(request, request.user)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('apps:index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('apps:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)