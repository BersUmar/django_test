from django.shortcuts import render

from dogs.models import Breed, Dog


# Create your views here.
def index(request):

    context = {
        'object_list': Dog.objects.all()[:3],
        'title': 'Питомник - наши породы'
    }
    return render(request, 'dogs/index.html', context)

def breed(request):

    context = {
        'object_list': Breed.objects.all(),
        'title': 'Все наши породы'
    }
    return render(request, 'dogs/breed.html', context)
