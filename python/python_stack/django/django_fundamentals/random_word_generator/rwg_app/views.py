from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
counter = 0
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['random_word'] = get_random_string(length=14)
    request.session['count'] += 1
    return render(request, "index.html")

def reset(request):
    request.session.flush()
    return redirect('/')

def plus_one(request):
    # request.session['count']+=1
    return redirect('/')


