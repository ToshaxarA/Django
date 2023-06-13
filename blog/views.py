from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
request = HttpRequest
response = HttpResponse
# Create your views here.

def index(request):
    return render(request, "blog/index.html")

# def test_page(request):
#     return HttpResponse("Test", status=404)

def contacts(request):
    return render(request, "blog/contacts.html")

def about(request):
    return render(request, "blog/about.html")

