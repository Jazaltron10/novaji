from django.shortcuts import redirect, render
from django.contrib.auth import login
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from .forms import UserForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("user-list")
    else:
        form = UserForm()
    return render(request, "onlineform/registration.html", {"form": form})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]  # Make sure only authenticated users can access this
