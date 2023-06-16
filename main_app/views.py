from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Poke, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Poke.objects.all()
    return render(request, 'pokemon/index.html', {
        'pokemon': pokemon
    })

def pokemon_detail(request, poke_id):
    poke = Poke.objects.get(id=poke_id)
    # Get the toys the poke doesn't have...
    # First, create a list of the toy ids that the poke DOES have
    id_list = poke.toys.all().values_list('id')
    # Now we can query for toys whose ids are not in the list using exclude
    toys_poke_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'pokemon/detail.html', {
        'poke': poke, 'feeding_form': feeding_form,
        # Add the toys to be displayed
        'toys': toys_poke_doesnt_have
    })

def assoc_toy(request, poke_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Poke.objects.get(id=poke_id).toys.add(toy_id)
    return redirect('detail', poke_id=poke_id)

def remove_toy(request, poke_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Poke.objects.get(id=poke_id).toys.remove(toy_id)
    return redirect('detail', poke_id=poke_id)

class PokeCreate(CreateView):
    model = Poke
    # Refactor fields so that 'toys' is not rendered in form
    fields = ['name', 'breed', 'description', 'age']

class PokeUpdate(UpdateView):
    model = Poke
    fields = ['breed', 'description', 'age']

class PokeDelete(DeleteView):
    model = Poke
    success_url = '/pokemon'

def add_feeding(request, poke_id):
    # create a ModelForm instance using 
    # the data that was submitted in the form
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # We want a model instance, but
        # we can't save to the db yet
        # because we have not assigned the
        # poke_id FK.
        new_feeding = form.save(commit=False)
        new_feeding.poke_id = poke_id
        new_feeding.save()
    return redirect('detail', poke_id=poke_id)

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'