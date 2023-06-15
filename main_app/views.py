from django.shortcuts import render

# Import the Poke Model
from .models import Poke

pokemon = [
  {'name': 'Gumbus', 'breed': 'Fuecoco', 'description': 'It lies on warm rocks and uses the heat absorbed by its square-shaped scales to create fire energy.', 'age': 1},
  {'name': 'Bingle', 'breed': 'Mudkip', 'description': 'Its large tail fin propels it through water with powerful acceleration. It is strong in spite of its size.', 'age': 2},
]

# Create your views here.
# Define the home view
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

# def pokemon_index(request):
#     # We pass data to a template very much like we did in Express!
#     return render(request, 'pokemon/index.html', {
#         'pokemon': pokemon
# })

def pokemon_index(request):
    pokemon = Poke.objects.all() # Retrieve all pokemon
    return render(request, 'pokemon/index.html',
    {
        'pokemon': pokemon
    }
)

def pokemon_detail(request, poke_id):
    poke = Poke.objects.get(id=poke_id)
    return render(request, 'pokemon/detail.html', { 'poke': poke })