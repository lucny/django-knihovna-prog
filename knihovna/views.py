from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from .forms import KnihaForm, AutorForm
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



class KnihaCreateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, CreateView):
    model = Kniha
    # template_name = 'kniha/book_form_simple.html'
    template_name = 'kniha/book_form_crispy.html'
    form_class = KnihaForm
    success_url = reverse_lazy('index')
    permission_required = ["knihovna.add_kniha"]

    def get_initial(self):
        initial = super().get_initial()
        initial['next'] = self.request.META.get('HTTP_REFERER', self.success_url)
        initial['editor'] = self.request.user
        return initial

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().post(request, *args, **kwargs)


class KnihaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Kniha
    template_name = 'kniha/book_form_crispy.html'
    form_class = KnihaForm
    context_object_name = 'book'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'
    permission_required = ["knihovna.change_kniha"]

    def get_initial(self):
        initial = super().get_initial()
        initial['next'] = self.request.META.get('HTTP_REFERER', self.success_url)
        return initial

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().post(request, *args, **kwargs)

    def test_func(self):
        kniha = self.get_object()
        return kniha.editor == self.request.user


class KnihaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Kniha
    template_name = 'kniha/book_confirm_form.html'
    success_url = reverse_lazy('index')
    context_object_name = 'book'
    pk_url_kwarg = 'pk'
    permission_required = ["knihovna.delete_kniha"]

    def get_initial(self):
        initial = super().get_initial()
        initial['next'] = self.request.META.get('HTTP_REFERER', self.success_url)
        return initial

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def test_func(self):
        kniha = self.get_object()
        return kniha.editor == self.request.user


class AutorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Autor
    # template_name = 'kniha/book_form_simple.html'
    template_name = 'autor/autor_form_crispy.html'
    form_class = AutorForm
    success_url = reverse_lazy('index')
    permission_required = ["knihovna.add_autor"]

    def get_initial(self):
        initial = super().get_initial()
        initial['next'] = self.request.META.get('HTTP_REFERER', self.success_url)
        initial['editor'] = self.request.user
        return initial

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().post(request, *args, **kwargs)


class AutorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Autor
    template_name = 'autor/autor_form_crispy.html'
    form_class = AutorForm
    context_object_name = 'autor'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'pk'
    permission_required = ["knihovna.change_autor"]

    def get_initial(self):
        initial = super().get_initial()
        initial['next'] = self.request.META.get('HTTP_REFERER', self.success_url)
        return initial

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel'):
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().post(request, *args, **kwargs)

    def test_func(self):
        autor = self.get_object()
        return autor.editor == self.request.user


class AutorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Autor
    template_name = 'autor/autor_confirm_form.html'
    success_url = reverse_lazy('index')
    context_object_name = 'autor'
    pk_url_kwarg = 'pk'
    permission_required = ["knihovna.delete_autor"]

    def test_func(self):
        autor = self.get_object()
        return autor.editor == self.request.user