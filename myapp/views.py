from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import HtmlVideo


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                videos = HtmlVideo.objects.all()

                return render(request, 'index.html', {'videos': videos})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    # Your view logic here
    return render(request, 'myapp/index.html')

@login_required
def restricted_view(request):
    # Your view logic here
    return render(request, 'index.html')



    return render(request, 'your_template.html', {'videos': videos})