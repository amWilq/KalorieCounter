from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date
from django.views.generic import DetailView
from .models import *
from django.template.defaulttags import register
from django.shortcuts import redirect
import datetime


class Edytujca_produktow(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Jedzenie
    template_name = 'base/produkty-edit.html'
    fields = ['date_eaten', 'name', 'total_calories', 'fat', 'protein', 'carbs', 'category']
    success_url = reverse_lazy('produkty_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):

    model = Jedzenie
    template_name = 'base/user_produkty.html'
    context_object_name = 'posts'
    paginate_by = 5


@property
def is_past_due(self):
    return date.today() > self.date


class DodajProdukt(LoginRequiredMixin, CreateView):
    model = Jedzenie
    fields = ['category', 'date_eaten', 'name', 'total_calories', 'fat', 'protein', 'carbs']
    context_object_name = 'calorie'
    success_url = reverse_lazy('produkty_list')
    template_name = 'base/produkty-dodaj.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProduktView(DetailView):
    model = Jedzenie
    context_object_name = 'produkty'
    template_name = 'base/produkty_detail.html'


class ProduktyView(LoginRequiredMixin, ListView):
    model = Jedzenie
    queryset = Jedzenie.objects.all().order_by('-total_calories')
    context_object_name = 'produkty'
    template_name = 'base/produkty_list.html'

    @register.filter
    def get_range(value):
        return range(1)

    def get_queryset(self):
        search_input = self.request.GET.get("ustaw-dzien", None) or 0
        today = datetime.datetime.now()
        if search_input:
            yesterday = today - datetime.timedelta(days=int(search_input))
            return Jedzenie.objects.filter(date_eaten=yesterday).filter(author=self.request.user)
        else:
            yesterday = today - datetime.timedelta(days=0)
            return Jedzenie.objects.filter(date_eaten=yesterday).filter(author=self.request.user)


class ProduktyDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jedzenie
    context_object_name = 'produkty'
    success_url = reverse_lazy('produkty_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def admin(request):
    return redirect('/admin/')
