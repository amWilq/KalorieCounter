from django.urls import path,include
from . import views
from .views import CalorieList,CalorieDetail,CalorieCreate,CalorieUpdate,CalorieDelete,Logowanie,Register,DodajProdukt,ProduktView,ProduktyView,ProduktyDelete
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserPostListView




urlpatterns = [
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('produkty/dodaj', DodajProdukt.as_view(), name='dodaj'),
    path('produkty/<int:pk>', ProduktView.as_view(), name='dodaj_view'),
    path('produkty', ProduktyView.as_view(), name='produkty_list'),
    path('produkty-delete/<int:pk>/', ProduktyDelete.as_view(), name='produkty-delete'),

    path('calorie/', CalorieList.as_view(), name='calories'),
    path('calorie/<int:pk>', CalorieDetail.as_view(), name='calorie'),
    path('calorie_create/', CalorieCreate.as_view(), name='calorie-create'),
    path('calorie-update/<int:pk>/', CalorieCreate.as_view(), name='calorie-update'),
    path('calorie-delete/<int:pk>/', CalorieDelete.as_view(), name='calorie-delete'),
    path('login/', Logowanie.as_view(), name='login'),
    path('', Logowanie.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
]