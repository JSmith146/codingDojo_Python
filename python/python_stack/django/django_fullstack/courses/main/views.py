from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request,"index.html", context)

def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect("/courses")
    else:
        desc= Description.objects.create(content=request.POST["desc"])
        course = Course.objects.create(name= request.POST["name"],description=desc)
        course.save()
        return redirect("/courses")

def delete(request,id):
    if request.method=="GET":
        context = {
            'course':Course.objects.get(id=id)
        }
        return render(request,"delete.html",context)
    if request.method=="POST":
        course = Course.objects.get(id = id)
        course.delete()
        return redirect("/courses")

def comments(request,id):
    context = {
        'course':Course.objects.get(id = id)
    }
    return render(request, "comments.html",context)

def new_comment(request,id):
    if request.method =="POST":
        course = Course.objects.get(id=id)
        comment_text = request.POST["comment"]
        Comment.objects.create(content=comment_text, course=course)
        return redirect(f"/courses/{id}/comments")
        
