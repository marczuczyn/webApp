from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ankieta


class AnkietaList(ListView):
    model = Ankieta


class AnkietaDetail(DetailView):
    model = Ankieta


class AnkietaDelete(DeleteView):
    model = Ankieta
    success_url = reverse_lazy('ankieta_list')
