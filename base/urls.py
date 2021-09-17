from django.urls import path,include
from . import views
from .views import DodajProdukt,ProduktView,ProduktyView,ProduktyDelete
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserPostListView,Edytujca_produktow





urlpatterns = [
    path('', ProduktyView.as_view(), name='home'),
    path('admin', views.admin, name='ADMIN-page'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),

    path('produkty/dodaj/', DodajProdukt.as_view(), name='dodaj'),
    path('produkty/<int:pk>', ProduktView.as_view(), name='dodaj_view'),
    path('produkty', ProduktyView.as_view(), name='produkty_list'),
    path('produkty-delete/<int:pk>/', ProduktyDelete.as_view(), name='produkty-delete'),
    path('produkty-edit/<int:pk>/', Edytujca_produktow.as_view(), name='produkty-edit'),

]