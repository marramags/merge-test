urlpatterns = [
    path('', views.home, name='home'),  #http://localhost:8000
    path('about/', views.about, name='about'), #http://localhost:8000/about
    path('pokedex/', views.pokedex, name='pokedex'), #http://localhost:8000/pokedex
    path('pokedex/<int:pokemon_id>/', views.pokemon_detail, name='detail'), #http://localhost:8000/pokedex/1
    path('pokedex/create/', views.PokemonCreate.as_view(), name='create_pokemon'), #http://localhost:8000/createpokemon
    path('pokedex/<int:pk>/update/', views.PokemonUpdate.as_view(), name='update_pokemon'), #http://localhost:8000/updatepokemon
    path('pokedex/<int:pk>/delete/', views.PokemonDelete.as_view(), name='delete_pokemon'),
    path('pokedex/<int:pokemon_id>/add_battle/', views.add_battle, name='add_battle'),
]