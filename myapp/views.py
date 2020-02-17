# Add your views here
from django.http import HttpResponse


def ping(request):
    return HttpResponse('OK')
