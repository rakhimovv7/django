from django.shortcuts import render
from apps.base.models import Base
# Create your views here.

def index(request):
    base = Base.objects.latest('id')
    return render(request, 'index-dark.html', locals())


def about(request):
    return render(request, 'about-us-dark.html', locals())