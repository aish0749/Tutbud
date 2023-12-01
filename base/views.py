from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'design with me'},
    {'id': 3, 'name': 'frontend developers'},
]

context = {'rooms': rooms}
def home(request):
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html', context)

