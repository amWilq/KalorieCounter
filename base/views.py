from django.shortcuts import  redirect
from .models import Jedzenie
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from datetime import date


class UserPostListView(ListView):

    model = Jedzenie
    template_name = 'base/user_produkty.html' #
    context_object_name = 'posts'
    paginate_by = 5 #ilosc postów wyświetlanych na stornie

    def get_queryset(self):


        #date = Jedzenie.objects.get(date_eaten=)
        #user = Jedzenie.objects.get(id=23)

        user = Jedzenie.objects.all
        #user = Jedzenie.objects.filter(name='2')

        return Jedzenie.objects.filter(author=user).order_by('-date_eaten').first()



@property
def is_past_due(self):
    return date.today() > self.date


class DodajProdukt(LoginRequiredMixin,CreateView):
    model = Jedzenie
    fields = '__all__'
    context_object_name = 'calorie'
    success_url = reverse_lazy('produkty_list')
    template_name = 'base/dodaj.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DodajProdukt, self).form_valid(form)

class ProduktView(DetailView):
    model = Jedzenie
    context_object_name = 'produkty'    #w html tego potem używamy
    template_name ='base/produkty_detail.html'


class ProduktyView(ListView):
    model = Jedzenie
    #Jedzenie.objects.filter(date_eaten__gte=datetime.date(2011, 1, 1))
    queryset = Jedzenie.objects.all().order_by('-total_calories')

    #w html tego potem używamy
    template_name ='base/produkty_list.html'


class ProduktyDelete(LoginRequiredMixin, DeleteView):
    model = Jedzenie
    context_object_name = 'produkty'
    success_url = reverse_lazy('produkty_list')

class CalorieList(LoginRequiredMixin,ListView):
    model = Jedzenie#orginalnie Calorie
    context_object_name = 'calories'

    #template_name = 'base/calorie_list.html'

class CalorieDetail(LoginRequiredMixin,DetailView):
    model = Jedzenie#orginalnie Calorie
    context_object_name = 'calorie'
    template_name = 'base/calorie.html'

class CalorieCreate(LoginRequiredMixin,CreateView):
    model = Jedzenie#orginalnie Calorie
    fields = ['title','description','calorie']
    success_url = reverse_lazy('calories')
    template_name = 'base/calorie-create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CalorieCreate, self).form_valid(form)

class CalorieUpdate(LoginRequiredMixin,UpdateView):
    model = Jedzenie
    fields = ['title','description','calorie']
    context_object_name = 'calorie-UPDATE'
    success_url = reverse_lazy('calories')

class CalorieDelete(LoginRequiredMixin,DeleteView):
    model = Jedzenie #orginalnie Calorie
    context_object_name = 'calorie'
    success_url = reverse_lazy('calories')



class Register(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('calories')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)

    def get(self,*args, **kwargs):
        if (self.request.user.is_authenticated):
            return redirect('calories')
        return super(Register,self).get(*args,**kwargs)

class Logowanie(LoginView):
    template_name ='base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('calories')