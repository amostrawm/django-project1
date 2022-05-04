from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, n1, n2):
    n3 = n1 + n2
    return HttpResponse('<h1>A soma {} + {} = {}</h1>'.format(n1, n2, n3) +
                        '<h1>A divisão {} / {} = {}</h1>'.format(n1, n2, n3))
