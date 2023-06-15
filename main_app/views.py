from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Poke
from django.views.generic import ListView

class PokeList(ListView):
    model = Poke
    template_name = 'pokemon/index.html'

class PokeCreate(CreateView):
    model = Poke
    fields = '__all__'
    success_url = '/pokemon'


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

class PokeUpdate(UpdateView):
    model = Poke
    # Let's disallow the renaming of a poke by excluding the name field!
    fields = ['breed', 'description', 'age']

class PokeDelete(DeleteView):
    model = Poke
    success_url = '/pokemon'