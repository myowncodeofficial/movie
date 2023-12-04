from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import Movieform

# Create your views here.
def fun1(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html',context)
# def details(request, movie_id):
#     return HttpResponse('this is movie number %s' % movie_id)

def details(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request, 'nexpage.html', {'obj':movie})
def add_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        year = request.POST['year']
        img = request.FILES['img']
        movies = Movie(name=name,desc=desc,year=year,img=img)
        movies.save()
    return render(request, 'add_details.html')
def update(request,id):
    movie = Movie.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'movie':movie,'form':form})
def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')