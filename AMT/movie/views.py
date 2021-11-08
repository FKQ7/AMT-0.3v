from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import movie
# Create your views here.
def main(request):
    movie_content = movie.objects.all()
    context={
        'movies': movie_content
    }
    return render(request, 'movie/home.html', context)


def dynamicUrl(request, Name):
    obj = movie.objects.get(Name=Name)
    context={
        'obj': obj
    }
    return render(request, 'movie/movie.html', context)
