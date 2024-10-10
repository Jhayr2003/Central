from django.shortcuts import render

from typing import Any
from django.db.models.query import QuerySet
from .models import *
from django.views.generic import ListView
from django.template import *
# Create your views here.

#CLASE PROMOCION
class PromocionListView(ListView):
    model = Promocion
    template_name = "promociones.html"

#CLASE LOGIN
class LoginListView(ListView):
    model = Promocion
    template_name = "login_register.html"

