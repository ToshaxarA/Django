from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
request = HttpRequest
response = HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Main page")

def test_page(request):
    return HttpResponse("Test", status=404)

def contacts(request):
    return HttpResponse("Какая-нибудь строка с контактами")

def about(request):
    return HttpResponse("Какая-нибудь строка с информацией")

