from django.shortcuts import render, HttpResponse


# Create your views here.


def hello(request,):
    return HttpResponse('<head> <title>Teste</title> </head>' +
                        '<h1>Site Teste</h1>' +
                        '<body> Este é um site teste em Django </body>')
