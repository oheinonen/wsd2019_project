from django.contrib import admin
from django.urls import path, include
from .views import (
    GameDetailView,
    GameListView,
    GameCreateView,
    GameDeleteView,
    GameUpdateView,
    UserGameListView,
    HighscoreListView
    )
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:username>',UserGameListView.as_view(),name='user-stats' ),
    path('game/add/',GameCreateView.as_view(),name='game-add' ),
    path('game/<str:pk>/',GameDetailView.as_view(),name='game-detail' ),
    path('game/<str:pk>/highscore/', views.highscore,name='highscore' ),
    path('game/<str:pk>/buy/', views.buy, name='buy' ),
    path('game/<str:pk>/buy/success/',views.payment_success,name='detail_success'),
    path('game/<str:pk>/buy/cancel/',views.payment_cancel,name='detail_cancel'),
    path('game/<str:pk>/buy/error/',views.payment_error,name='detail_error'),
    path('game/<str:pk>/save/', views.gamestate,name='gamestate' ),
    path('game/<str:pk>/load/', views.loadgame,name='loadgame' ),
    path('game/<str:pk>/update/',GameUpdateView.as_view(),name='game-update'),
    path('game/<str:pk>/delete/',GameDeleteView.as_view(),name='game-delete'),
    path('browsegames/',views.games_list, name='browse_games' ),
    path('highscores/',HighscoreListView.as_view(),name='highscores' )
]
