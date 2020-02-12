from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from demo.forms import SignUpForm, LoginForm
from custom_user.models import MyCustomUser

@login_required()
def index(request):
    return render(request, 'index.html', {
        'user_type': str(type(MyCustomUser.objects.get(id=request.user.id)))
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    
    return render(request, 'generic_form.html', {'form': LoginForm()})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = MyCustomUser.objects.create_user(
                data['username'], data['email'], data['password1']
            )
            login(request, user)

            return HttpResponseRedirect(reverse('homepage'))
    
    return render(request, 'generic_form.html', {
        'form': SignUpForm()
    })