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

class GameCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Game
    fields = ['name', 'url', 'price']

    def form_valid(self,form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.usertype == "['dev']"

class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    fields = ['name', 'url', 'price']

    def form_valid(self,form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        game = self.get_object()
        return self.request.user == game.developer

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    success_url = '/'

    def test_func(self):
        game = self.get_object()
        return self.request.user == game.developer
