from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='index'),
    path('pokemon/<int:poke_id>/', views.pokemon_detail, name='detail'),
    path('pokemon/create/', views.PokeCreate.as_view(), name='pokemon_create'),
    path('pokemon/<int:pk>/update/', views.PokeUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.PokeDelete.as_view(), name='pokemon_delete'),
    path('pokemon/<int:poke_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # associate a toy with a poke (M:M)
    path('pokemon/<int:poke_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # remove toy from a pokemon
    path('pokemon/<int:poke_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]