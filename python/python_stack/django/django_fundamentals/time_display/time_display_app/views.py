from django.shortcuts import render, HttpResponse
import datetime
from time import gmtime, strftime

# Create your views here.

def index(request):
    context = {
        "date": datetime.datetime.now().date(),
        "time": datetime.datetime.now().time(),
    }
    return render(request, "index.html", context)