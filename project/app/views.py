from django.shortcuts import render
from multiprocessing import context
from .forms import UserForm

# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def create(request):
    if request.method == 'GET':
        form = UserForm()

        context = {
            'form': form
        }
        return render(request, 'user/create.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            context = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'bday': form.cleaned_data['bday'],
                'tax_number': form.cleaned_data['tax_number']
            }
    return render(request, 'user/index.html', context=context)
