from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def submission(request):
    request.session["form_name"]= request.POST['name']
    request.session["form_location"]= request.POST['location']
    request.session["form_language"]= request.POST['lang']
    request.session["form_comment"]= request.POST['comment']
    return redirect("/result")

def result(request):
    return render(request,"result.html")