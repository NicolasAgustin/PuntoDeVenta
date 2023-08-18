from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

from django.http import HttpRequest

from interfaz.forms import LoginForm

from interfaz.models import Client
from interfaz.services import auth_service

"""TODO:
    - Revisar autenticacion
    - Revisar permisos
    - Revisar manejo de errores
    - Revisar templating
    - Revisar session y contexto

"""


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Hello django")


def login(request: HttpRequest):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            try:
                auth_service.auth_user(form.cleaned_data)
            except Exception:
                form.add_error("username", "Usuario o contrasena incorrecta")
                form.add_error("password", "")
            else:
                return HttpResponseRedirect("/clients")
    else:
        form = LoginForm()

    return render(request, "interfaz/login.html", {"form": form})


def home(request: HttpRequest):

    if request.method == "GET":

        botones = ["Nueva venta", "Clientes", "Proveedor", "Productos", "Ventas", "Configuracion"]
        names = [x.lower().replace(" ", "_") for x in botones]

        return render(request, "interfaz/home.html", {"labels": zip(botones, names)})


def client(request, name):
    response = "Estas buscando el cliente llamado %s" % name
    return HttpResponse(response)


def clients(request):
    clients = Client.objects.all()

    context = {"clients": clients}

    return render(request, "interfaz/clients.html", context)
