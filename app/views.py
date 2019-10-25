from django.http import HttpResponse

import pydevd
pydevd.settrace()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")