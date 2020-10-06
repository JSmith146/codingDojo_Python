from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
# Create your views here.
def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request,"index.html", context)

def add_new_show(request):
    return render(request,"new_show_form.html")

def create_new_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/new")
    else:
        if request.method=="POST":
            Show.objects.create(
                title=request.POST["title"],
                network= request.POST["network"],
                release_date = request.POST['release_date'],
                desc = request.POST['desc']
            )
            show = Show.objects.last()
    return redirect(f"/shows/{show.id}") 

def display_show(request,id):
    context={
        'show': Show.objects.get(id = id)
    }
    return render(request,"display_show.html",context)

def edit_show(request, id):
    context={
        'show': Show.objects.get(id = id),
        'release_date': Show.objects.get(id=id).release_date.strftime("%Y-%m-%d")
    }

    return render(request,"edit_show.html",context)

def update_show(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
        if request.method=="POST":
            show = Show.objects.get(id=id)
            show.title = request.POST["title"]
            show.network = request.POST['network']
            show.release_date = request.POST['release_date']
            show.desc  = request.POST['desc']
            show.save()

    return redirect(f"/shows/{show.id}")

def delete_show(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect("/shows")