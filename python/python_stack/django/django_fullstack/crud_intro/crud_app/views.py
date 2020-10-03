from django.shortcuts import render, HttpResponse, redirect
from .models import Dog

# Create your views here.
def index(request):
    context = {
        'all_dogs': Dog.objects.all()
    }
    return render(request, 'index.html', context)

def create_form(request):
    return render(request, 'create.html')

def create_dog(request):
    #create instance of dog class
    if request.method == "POST":
        print(request.POST)
        Dog.objects.create(name= request.POST['dog_name'], age = request.POST['age'])
    return redirect('/')

def show_dog(request, id):
    #show one instance of a Dog on a template
    context = {
        "one_dog":Dog.objects.get(id = id)
    }
    return render(request, 'one_dog.html', context)

def delete_dog(request, id):
    if request.method =="POST":
        dog_to_delete = Dog.objects.get(id=id)
        dog_to_delete.delete()
    return redirect("/")
    

def edit_dog(request, id):
    #Show a form to edit a dog instance
    context = {
        'one_dog_edit': Dog.objects.get(id=id)
    }

    return render(request, "edit.html", context)

def update_dog(request, id):
    if request.method == "POST":
        dog_to_update = Dog.objects.get(id=id)
        dog_to_update.name = request.POST['dog_name']
        dog_to_update.age = request.POST['age']
        dog_to_update.save()
    return redirect(f"/dogs/{id}")