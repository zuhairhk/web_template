from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import Video_form
from .models import Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# video data type
all_video = Video

# used to display required data on homepage
def index(request):
    all_video = Video.objects.all
    currentUser = request.user

    # takes in information of available videos and displayes them if they are valid
    if request.method == 'POST':
        form = Video_form(data = request.POST, files= request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Video_form()

    return render(request, 'index.html', {'form' : form, 'all': all_video, 'username': currentUser})

# handles uploading videos
def upload(request):
    all_video = Video.objects.all

    if request.method == 'POST':
        # sends form to front-end
        form = Video_form(data = request.POST, files= request.FILES)
        
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = Video_form()

    return render(request, 'upload.html', {'form' : form, 'all': all_video})

# registers user
def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# logs in user
def signIn(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if form.is_valid():
            # form.save()
            login(request, user)

            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# logs out user
def disconnect(request):
    logout(request)

    return redirect('login')