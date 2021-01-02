from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('clients', views.clients, name='clients'),
    path('transactions', views.transactions, name='transactions'),
    path('add-client', views.add_client, name='add_client'),
    path('add-transaction', views.add_transaction, name='add_transaction'),
] 