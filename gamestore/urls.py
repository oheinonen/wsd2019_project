from django.contrib import admin
from django.urls import path, include
from .views import (
    GameDetailView,
    GameListView,
    GameCreateView,
    GameDeleteView
        )
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/add/',GameCreateView.as_view(),name='game-add' ),
    path('game/<str:pk>/',GameDetailView.as_view(),name='game-detail' ),
    #path('game/<str:pk>/update/',GameUpdateView.as_view(),name='game-update'),
    path('game/<str:pk>/delete/',GameDeleteView.as_view(),name='game-delete')

]
