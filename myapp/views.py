from django.shortcuts import render, HttpResponse
from .models import Elespectador


# Create your views here.
def index(request,pk=None):
	objs = Elespectador.objects.filter(category=pk)
	return render(request, "myapp/index.html", {'objs':objs})

def landing(request):
	return render(request, "myapp/index.html")
	