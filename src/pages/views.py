from django.shortcuts import render
from django.http import HttpResponse

from person.models import Person

# Create your views here.
def home_view(request, *arg, **kwargs):

    queryset = Person.objects.all()
    my_context = {
        'object_list': queryset,
        'is_auth': request.user.is_authenticated
    }
    
    return render(request, 'home.html', my_context)

    # return HttpResponse('<h1 align="center">Hello ' + str(request.user) + ' !</h1>')

def about_view(request, *args, **kwargs):
    description = ''
    if request.user.is_authenticated:
        description = 'You are awesome cause you are logged in !'
    else:
        description = "Who the hell are you ?!"
    my_context = {
        'info': description,
        'year': 2021,
        "games_made":['In the woods', 'Winding Bird', 'Mission: Rush']
    }
    return render(request, 'about.html', my_context)