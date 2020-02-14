from django.contrib import admin
from django.urls import path, include
from .views import (
    GameDetailView,
    GameCreateView,
    GameDeleteView,
    GameUpdateView,
    BrowseGamesView,
    SearchGamesView,
    UserGameListView,
    HighscoreListView
    )
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:username>',UserGameListView.as_view(),name='user-stats' ), #domain/user/johndoe
    path('game/add/',GameCreateView.as_view(),name='game-add' ), #domain/game/add
    path('game/<str:pk>/',GameDetailView.as_view(),name='game-detail' ), #domain/game/snake
    path('game/<str:pk>/highscore/', views.highscore,name='highscore' ), #domain/game/snake/highscore
    path('game/<str:pk>/buy/', views.buy, name='buy' ), #domain/game/snake/buy
    path('game/<str:pk>/buy/success/',views.payment_success,name='detail_success'), #domain/game/snake/success = payment was succesfull
    path('game/<str:pk>/buy/cancel/',views.payment_cancel,name='detail_cancel'), #domain/game/snake/cancel = payment was cancelled
    path('game/<str:pk>/buy/error/',views.payment_error,name='detail_error'), #domain/game/snake/error = payment resulted in error
    path('game/<str:pk>/save/', views.gamestate,name='gamestate' ), #domain/game/snake/save = saving the game
    path('game/<str:pk>/load/', views.loadgame,name='loadgame' ), #domain/game/snake/load = loading the game
    path('game/<str:pk>/update/',GameUpdateView.as_view(),name='game-update'), #domain/game/snake/update = update the game
    path('game/<str:pk>/delete/',GameDeleteView.as_view(),name='game-delete'), #domain/game/snake/delete = delete the game
    path('browsegames/',BrowseGamesView.as_view(), name='browse_games' ), #domain/browsegames = browse available games
    path('search/',SearchGamesView.as_view(), name='search' ), #domain/search/ = search games
    path('highscores/',HighscoreListView.as_view(),name='highscores' ) #domain/highscores = list of all highscores
]
