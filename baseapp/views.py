from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
# to into Q for query search
from django.db.models import Q
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#for flash messages
from django.contrib import messages
# rooms = [
#     {'id': 1, 'name': 'Let\'s learn c#'},
#     {'id': 2, 'name': 'Let\'s learn html'},
#     {'id': 3, 'name': 'Let\'s learn Javascript'}
# ]

# Create your views here.

#login page
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: #to check if a user exists
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist, Try Registering ")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Password is incorrect")
    context = {}
    return render(request, 'baseapp/login_register.html', context)

#Logout page
def LogoutPage(request):
    logout(request)
    return redirect('login')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(description__icontains=q) |
        Q(name__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms' : rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'baseapp/index.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'baseapp/room.html', context)

@login_required(login_url="login")
def CreateRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'baseapp/form_list.html', context)


@login_required(login_url="login")
def UpdateRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'baseapp/form_list.html', context)


@login_required(login_url="login")
def DeleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'baseapp/delete.html', {'obj':room})


