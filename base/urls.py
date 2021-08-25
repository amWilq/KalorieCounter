from django.urls import path,include
from . import views
from .views import Logowanie,Register,DodajProdukt,ProduktView,ProduktyView,ProduktyDelete
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserPostListView,Edytujca_produktow





urlpatterns = [
    path('', Logowanie.as_view(), name='login'),
    path('login/', Logowanie.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    path('produkty/dodaj/', DodajProdukt.as_view(), name='dodaj'),
    path('produkty/<int:pk>', ProduktView.as_view(), name='dodaj_view'),
    path('produkty', ProduktyView.as_view(), name='produkty_list'),
    path('produkty-delete/<int:pk>/', ProduktyDelete.as_view(), name='produkty-delete'),
    path('produkty-edit/<int:pk>/', Edytujca_produktow.as_view(), name='produkty-edit'),

]