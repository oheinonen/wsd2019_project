from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Game,Highscore, GameSession
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

def buy(request, pk):
    template_name = 'gamestore/buy.html'
    context = {
        'game': Game.objects.filter(name=pk).first()
    }
    return render(request, "gamestore/buy.html",context)


def gamestate(request, pk):
    if request.method == "GET":
        game = Game.objects.filter(name=pk).first()
        try:
            oldGameSave = GameSession.objects.get(game=game, player=request.user)
            oldGameSave.delete()
        except GameSession.DoesNotExist:
            pass
        gs = GameSession( game=game,player=request.user, gameState=request.GET['gameState'])
        gs.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccessful")

def highscore(request, pk):
    if request.method == "GET":
        game = Game.objects.filter(name=pk).first()
        hs = Highscore( game=game,player=request.user, score = request.GET['score'] )
        hs.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccessful")

def loadgame(request, pk):
    if request.method == "GET":
        game = Game.objects.filter(name=pk).first()
        gameSave = GameSession.objects.get(game=game, player=request.user)

        if gameSave == None:
            return HttpResponse("unsuccessful")
        else:
            return HttpResponse(gameSave.gameState)

    else:
        return HttpResponse("unsuccessful")


def games_list(request):
    context = {
        'games' : Game.objects.all()
    }
    return render(request, 'gamestore/browse_games.html', context)

class GameListView(ListView):
    model = Game
    template_name = 'gamestore/browse_games.html'
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super(HighscoreListView, self).get_context_data(**kwargs)
        context.update({
            'games': Game.objects.all()
        })
        return context

    def get_queryset(self):
        return Highscore.objects.order_by('-score')

class HighscoreListView(ListView):
    model = Highscore
    template_name = 'gamestore/highscores.html'
    context_object_name = 'highscores'

    def get_context_data(self, **kwargs):
        context = super(HighscoreListView, self).get_context_data(**kwargs)
        context.update({
            'games': Game.objects.all()
        })
        return context

    def get_queryset(self):
        return Highscore.objects.order_by('-score')

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
