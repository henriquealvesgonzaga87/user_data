from django.shortcuts import render, redirect
from multiprocessing import context
from .forms import UserForm
from .models import *

# Create your views here.


def index(request):
    try:
        users = User.objects.all()
        context = {'users': users}
    except Exception:
        return "We're having problems to load the system. Sorry!"
    else:
        return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        try:
            form = UserForm()

            context = {
                'form': form
            }
        except Exception:
            return "We're having problems to load the system. Sorry!"
        else:
            return render(request, 'create.html', context=context)
    else:
        try:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
        except Exception:
            return "We're having problems to load the system. Sorry!"
        else:
            return redirect(index)


def modify(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        try:
            form = UserForm(data=request.POST, instance=user)
            if form.is_valid():
                form.save()
        except Exception:
            return "We're having problems to load the system. Sorry!"
        else:
            return redirect(index)
    else:
        try:
            form = UserForm(instance=user)
            context = {'form': form}
        except Exception:
            return "We're having problems to load the system. Sorry!"
        else:
            return render(request, 'create.html', context=context)

def delete(request, user_id):
    pass
