from django.shortcuts import render, redirect
from .models import Show
import datetime

# Create your views here.
def index(request):
    context={
        'all_shows': Show.objects.all()
    }
    return render(request,"index.html", context)

def add_new_show(request):
    return render(request,'create_show.html')

def create_show(request):
    if request.method=="POST":
        Show.objects.create(
            title = request.POST["title"],
            network = request.POST["network"],
            release_date = request.POST["release_date"], 
            desc = request.POST['desc']
            )
        # context = {
        #     'show': Show.object.last()
        # }
        show = Show.objects.last()
    return redirect(f"/show/{show.id}")

def display_show(request,id):
    #display one instance of a Show template
    context={
        'show':Show.objects.get(id=id)
    }
    return render(request, "show.html", context)
        
def edit_show(request,id):
    context={
        'show': Show.objects.get(id=id),
        'release_date': Show.objects.get(id=id).release_date.strftime("%Y-%m-%d")
    }
    return render(request,"edit_show.html",context)

def update_show(request, id):
    if request.method=="POST":
        show_to_update = Show.objects.get(id=id)
        show_to_update.title = request.POST["title"]
        show_to_update.network = request.POST["network"]
        show_to_update.release_date = request.POST["release_date"]
        show_to_update.desc = request.POST["desc"]
        show_to_update.save()
    return redirect(f"/show/{id}")

def delete_show(request, id):
    # if request.method == "POST":
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect("/")
