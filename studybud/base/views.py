from django.shortcuts import render
from django.http import HttpResponse

rooms = { 
    {"id":1, "name":"lets learn pyhton"},
    {"id":2, "name":"design with me"},
    {"id":3, "name":"front end dev "},
}
def home(request):
    return render(request,"home.html", {"rooms":rooms})
def room(request):
    return render(request,"room.html")