from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

# def result(request):
#     return render(request, "result.html")

def submission(request):
    context ={
        "form_name": request.POST['name'],
        "form_location": request.POST['location'],
        "form_language": request.POST['lang'],
        "form_comment": request.POST['comment']
    }
    return render(request, "result.html",context)