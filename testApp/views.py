from django.shortcuts import render

# Create your views here.
def homeView(request):

    return render(request, 'testApp/home.html')

def moviesView(request):

    return render(request, 'testApp/movies.html')

def sportsView(request):

    return render(request, 'testApp/sports.html')

def politicsView(request):

    return render(request, 'testApp/politics.html')
