from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Game
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import requests
# Create your views here.

def home(request):
    context = {
        'games' : Game.objects.all()
    }
    return render(request, "home.html",context)

class GameListView(ListView):
    model = Game
    template_name = 'home.html'
    context_object_name = 'games'

class GameDetailView(DetailView):
    model = Game
