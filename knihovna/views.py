from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from .forms import KnihaForm
from .models import Kniha, Zanr, Autor


def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('-rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


def authors(request):
    context = {
        'autori': Autor.objects.all(),
    }
    return render(request, 'authors.html', context=context)


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor/detail.html'
    context_object_name = 'author'


class KnihaListView(ListView):
    model = Kniha
    template_name = 'kniha/list.html'
    context_object_name = 'books'


class KnihaDetailView(DetailView):
    model = Kniha
    template_name = 'kniha/detail.html'
    context_object_name = 'kniha'


def knihy_podle_zanru(request, id):
    context = {
        'knihy': Kniha.objects.order_by('titul').filter(zanry__id=id),
        'zanr': Zanr.objects.get(pk=id)
    }
    return render(request, 'kniha/zanr.html', context=context)


class KnihaCreateView(CreateView):
    model = Kniha
    template_name = 'kniha/book_form.html'
    form_class = KnihaForm
    success_url = reverse_lazy('index')


class KnihaUpdateView(UpdateView):
    model = Kniha
    template_name = 'kniha/book_form_crispy.html'
    form_class = KnihaForm
    context_object_name = 'book'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'


class KnihaDeleteView(DeleteView):
    model = Kniha
    template_name = 'kniha/book_confirm_form.html'
    success_url = reverse_lazy('index')
    context_object_name = 'book'
    pk_url_kwarg = 'pk'