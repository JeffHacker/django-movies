from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound
from mov_rate.models import Movie, Rating



def list_o_movies(request):
    movielist = Movie.objects.all()
    context = {"movies": movielist}
    return render_to_response("movie_list.html", context)


def top_twenty(request):
    #toptwenty = Rating.objects.filter
    #context = {"movies": toptwenty}
    #return render_to_response('top_twenty.html', {context})
    pass

