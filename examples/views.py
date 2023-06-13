from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
request = HttpRequest
response = HttpResponse
# Create your views here.
# Функциональный обработчик(view), принимает request, отдаёт responce
# def index(request):
#     return HttpResponse("Hello!")

# def index(request):
#     my_list = [1,2,3,4]
#     return HttpResponse(my_list)

# def index(request):
#     text = "<h1>Hello</h1>"
#     return HttpResponse(text)

# def index(request):
#     text = "<h1>Hello</h1>"
#     return HttpResponse(text)

# Передача заголовков ответа
# def index(request):
#     headers = {
#         "Name":"Alex",
#     }
#     return HttpResponse("Hello", headers=headers)

# def index(request):
#     return HttpResponse()

# def index(request):
#     my_data = "File"
#     headers ={
#         'Content-Type':'application/vnd.ms-excel',
#         'Content-Disposition': 'attachment; filename=test.xls',
#     }
    
#     return HttpResponse(my_data, headers=headers)


# def index(request):
#     print(request.GET)
#     if request.method == "GET":
#         print(request.get_host())
#     return HttpResponse("Hello!", status=500)
