from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ankieta
from .forms import AnkietaForm


class AnkietaList(ListView):
    model = Ankieta


class AnkietaDetail(DetailView):
    model = Ankieta


class AnkietaDelete(DeleteView):
    model = Ankieta
    success_url = reverse_lazy('ankieta_list')


class AnkietaCreate(CreateView):
    model = Ankieta
    form_class = AnkietaForm
    success_url = reverse_lazy('ankieta_list')
    # fields = ['wiek', 'wzrost', 'plec', 'kolor']


class AnkietaEdit(UpdateView):
    model = Ankieta
    form_class = AnkietaForm
    # success_url = reverse_lazy('ankieta_detail')
    # fields = ['wiek', 'wzrost', 'plec', 'kolor']
    template_name = 'ankieta/ankieta_edit.html'

    def get_success_url(self):
        return reverse_lazy('ankieta_detail', kwargs={'pk': self.kwargs['pk']})
