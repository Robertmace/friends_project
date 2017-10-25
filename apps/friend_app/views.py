# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User

# Create your views here.

def index(request):
    context = {
    'users': User.objects.all(),
    'friends': User.objects.get(id= request.session['id']).friends.all()
    }
    return render(request, 'friend_app/index.html', context)

def show(request, id):
    context = {
    'other_user': User.objects.get(id=id)
    }
    return render(request, 'friend_app/show.html', context)
def showFriend(request, id):
    context = {
    'other_user': User.objects.get(id=id)
    }
    return render(request, 'friend_app/show.html', context)

def addFriend(request, id):
    User.objects.get(id= request.session['id']).friends.add(User.objects.get(id = id))
    return redirect('/friend')

def remFriend(request, id):
    User.objects.get(id= request.session['id']).friends.remove(User.objects.get(id = id))
    return redirect('/friend')

def edit(request, id):
    context = {
    'user': User.objects.get(id=id)
    }
    return render(request, "friend_app/edit.html", context)

def update(request, id):
    user1 = User.objects.get(id=id)
    user1.first_name = request.POST['first_name']
    user1.last_name = request.POST['last_name']
    user1.email = request.POST['email']
    user1.save()

    return redirect('/friend')


def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/friend')