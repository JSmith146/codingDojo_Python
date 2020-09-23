from django.shortcuts import render, HttpResponse, redirect
from .models import Users

# Create your views here.
def index(request):
    context={
        'users': Users.objects.all()
    }
    return render(request,'index.html',context)

def submission(request):
    Users(
        name = " ".join([request.POST["fname"], request.POST["lname"]]),
        email = request.POST["email"],
        age = request.POST["age"]
    ).save()
    return redirect('/')