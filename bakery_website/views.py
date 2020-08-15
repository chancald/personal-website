from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = (
        "<html><body><h1>Imagine there's a list of blog posts here!</h1></body></html>"
    )
    return HttpResponse(html, charset="utf-8")
