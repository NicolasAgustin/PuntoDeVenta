from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.http import HttpRequest

from interfaz.forms import LoginForm

from interfaz.models import Client

"""TODO:
    - Revisar autenticacion
    - Revisar bootstrap
    - Revisar permisos
    - Revisar manejo de errores
    - Revisar templating

"""


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Hello django")


def login(request: HttpRequest):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/clients")
    else:
        form = LoginForm()

    return render(request, "interfaz/login.html", {"form": form})

def client(request, name):
    response = "Estas buscando el cliente llamado %s" % name
    return HttpResponse(response)


def clients(request):
    clients = Client.objects.all()

    context = {"clients": clients}

    return render(request, "interfaz/clients.html", context)