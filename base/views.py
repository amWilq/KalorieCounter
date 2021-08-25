from .forms import ExampleForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from datetime import date
from django.shortcuts import  redirect
from django.views import generic
from django.views.generic import DetailView
from .models import *
from django.http import HttpResponse
from django.http import Http404

from django.utils.translation import ugettext as _


from django.shortcuts import render, redirect
from .forms import ExampleForm
from datetime import timedelta

from .forms import Homeform




class Edytujca_produktow(generic.UpdateView):
    model = Jedzenie
    template_name = 'base/produkty-edit.html'
    fields = ['date_eaten','name', 'total_calories', 'fat', 'protein', 'carbs','category']

    success_url = reverse_lazy('produkty_list')


class UserPostListView(ListView):

    model = Jedzenie
    template_name = 'base/user_produkty.html' #
    context_object_name = 'posts'
    paginate_by = 5 #ilosc postów wyświetlanych na stornie

@property
def is_past_due(self):
    return date.today() > self.date

class DodajProdukt(LoginRequiredMixin,CreateView):
    model = Jedzenie
    fields = '__all__'
    context_object_name = 'calorie'
    success_url = reverse_lazy('produkty_list')
    template_name = 'base/produkty-dodaj.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DodajProdukt, self).form_valid(form)

class ProduktView(DetailView):
    model = Jedzenie
    context_object_name = 'produkty'    #w html tego potem używamy
    template_name ='base/produkty_detail.html'


class ProduktyView(LoginRequiredMixin,ListView):
    model = Jedzenie
    queryset = Jedzenie.objects.all().order_by('-total_calories')

    #w html tego potem używamy

    template_name ='base/produkty_list.html'

    def search(request):
        if request.GET.get('q'):
            message = 'You submitted: %r' % request.GET['q']
        else:
            message = 'You submitted nothing!'

        return HttpResponse(message)


    def get_queryset(self):
        import datetime

        search_input  = self.request.GET.get("ustaw-dzien", None) or 0

        if search_input:
            yesterday = datetime.datetime.now() - datetime.timedelta(days=int(search_input))
            return Jedzenie.objects.filter(date_eaten=yesterday).filter(author=self.request.user)
        else:
            yesterday = datetime.datetime.now() - datetime.timedelta(days=0)
            return Jedzenie.objects.filter(date_eaten=yesterday).filter(author=self.request.user)



    #def home(request):
    #    if request.method == 'GET':
    #        return render(request, 'test_app/home.html', {'form': ExampleForm()})
    #    else:
    #        form = ExampleForm(request.POST)
    #        if form.is_valid():
    #            t = form.cleaned_data['time']
    #
    #           t2 = timedelta(hours=1)
    #
    #            print(t, type(t))
    #            print(t2, type(t2))
    #
    #           return redirect('home')



class ProduktyDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Jedzenie
    context_object_name = 'produkty'
    success_url = reverse_lazy('produkty_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class Register(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('produkty_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)

    def get(self,*args, **kwargs):
        if (self.request.user.is_authenticated):
            return redirect('produkty_list')
        return super(Register,self).get(*args,**kwargs)

class Logowanie(LoginView):
    template_name ='base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('produkty_list')