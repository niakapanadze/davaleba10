from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def films(request):
    films_list = [
        {"title" : "Brand New Day", "imdb": 7.9},
        {"title" : "The Maze Runner", "imdb": 8.1},
        {"title": "The Joker", "imdb": 7.5},
    ]
    context = {"films" : films_list}
    return render(request, 'films.html', context)
