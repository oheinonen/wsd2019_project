from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Game,Highscore
from users.models import CustomUser
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

def highscore(request, pk):
    if request.method == "GET":
        game = Game.objects.filter(name=pk).first()
        hs = Highscore( game=game,player=request.user, score = request.GET['score'] )
        hs.save()
        return HttpResponse('success')

class GameListView(ListView):
    model = Game
    template_name = 'home.html'
    context_object_name = 'games'

class UserGameListView(ListView):
    model = Game
    template_name = 'gamestore/user_stats.html'
    context_object_name = 'games'

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        return Game.objects.filter(developer=user)

class GameDetailView(DetailView):
    model = Game
    template_name = 'gamestore/detail.html'

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
