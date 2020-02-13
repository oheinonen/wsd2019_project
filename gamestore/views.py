from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Game,Highscore, GameSession, Transaction
from users.models import CustomUser
from django.db.models import Q
from hashlib import md5
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
        'games' :Game.objects.all(),
        'home_page' : 'active'
    }

    return render(request, "home.html", context)


def buy(request, pk):
    template_name = 'gamestore/buy.html'
    game = Game.objects.filter(name=pk).first()
    user = request.user
    transaction = Transaction(game=game, player=user)
    transaction.save()
    secret = 'cpWS7GVBRKk6zkAOx58eL6JmyvYA'
    checksumstr = f"pid={str(transaction.id):s}&sid=6aBk9HRlc3RTZWxsZXI=&amount={game.price:.2f}&token={secret:s}"
    checksum = md5(checksumstr.encode('utf-8')).hexdigest()

    successurl = request.build_absolute_uri(game.get_absolute_url()+'buy/success')
    errorurl = request.build_absolute_uri(game.get_absolute_url()+'buy')
    cancelurl = request.build_absolute_uri(game.get_absolute_url()+'buy/cancel')

    context = {
        'game': game,
        'user': user,
        'transaction': transaction,
        'checksum': checksum,
        'successurl': successurl,
        'errorurl': errorurl,
        'cancelurl': cancelurl
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

def payment_success(request,pk):
    game=Game.objects.filter(name=pk).first()
    context = {
        'game': game,
        'message': "Game successfully purchased!",
        'highscores': Highscore.objects.order_by('-score')
    }
    url = request.build_absolute_uri(game.get_absolute_url())

    if game in request.user.games.all():
        context['message'] = "You have already bought this game!"
        return redirect(url, context)

    else:
        request.user.games.add(game)
        return redirect(url, context)

def payment_cancel(request,pk):

    game=Game.objects.filter(name=pk).first()
    context = {
        'game': game,
        'message': "Payment cancelled!",
        'highscores': Highscore.objects.order_by('-score')
    }
    url = request.build_absolute_uri(game.get_absolute_url())
    return redirect(url, context)

def payment_error(request,pk):
    game=Game.objects.filter(name=pk).first()
    context = {
        'game': game,
        'message': "Error occured during payment. Try again or contact us.",
        'highscores': Highscore.objects.order_by('-score')
    }
    url = request.build_absolute_uri(game.get_absolute_url())
    return render(url, context)

class BrowseGamesView(ListView):
    model = Game
    template_name = 'gamestore/browse_games.html'
    context_object_name = 'games'

class SearchGamesView(ListView):
    model = Game
    template_name = 'gamestore/search.html'
    context_object_name = 'games'

    def get_queryset(self):
        if self.request.method=='GET':
            q = self.request.GET.get('q')
            games = Game.objects.filter(
                Q(name__icontains=q)
                ).distinct()
        else:
            games = Game.objects.all()
        return games


class HighscoreListView(ListView):
    model = Highscore
    template_name = 'gamestore/highscores.html'
    context_object_name = 'highscores'

    def get_context_data(self, **kwargs):
        context = super(HighscoreListView, self).get_context_data(**kwargs)
        context.update({
            'games': Game.objects.all(),
            'highscore_page' : 'active'
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

    def get_context_data(self, **kwargs):
        context = super(UserGameListView, self).get_context_data(**kwargs)
        context.update({
            'transactions': Transaction.objects.all(),
            'sales_stats_page' : 'active'

        })
        return context

class GameDetailView(DetailView):
    model = Game
    template_name = 'gamestore/detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context.update({
            'highscores': Highscore.objects.order_by('-score')
        })
        return context


class GameCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Game
    fields = ['name', 'url', 'price']

    def form_valid(self,form):
        form.instance.developer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.usertype == "['dev']"

    def get_context_data(self, **kwargs):
        context = super(GameCreateView, self).get_context_data(**kwargs)
        context.update({
            'add_game_page' : 'active'
        })
        return context

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
