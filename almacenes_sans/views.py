from django.shortcuts import render
from loginapp.models import usuario
# Create your views here.
def home(request):
    return render(request, "gestionproducto.html", {})