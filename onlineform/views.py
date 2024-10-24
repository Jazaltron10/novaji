# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserForm



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User = form.save()
            login(request, User)
            return redirect("login/")
    else:
        form = UserForm()
    return render(request, "onlineform/register.html", {"form":form})
            
        

@login_required
class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    