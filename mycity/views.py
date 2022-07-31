from django.shortcuts import render, redirect
from mycity.models import Citizen
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def index(request):  
    citizens = Citizen.objects.order_by('id').all()
    context = {'citizens': citizens}
    return render(request, 'mycity/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'mycity/index.html')
