from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Client, Transaction
from .forms import AddClientForm, AddTransactionForm

@login_required(login_url='login')
def home(request):
    clients = Client.objects.all()[:5]
    transactions = Transaction.objects.all()[:5]
    context = {
        'clients': clients,
        'transactions': transactions,
    }
    return render(request, 'ctapp/home.html', context=context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'ctapp/login.html')

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, 'ctapp/clients.html', context)

@login_required(login_url='login')
def transactions(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions,
    }
    return render(request, 'ctapp/transactions.html', context=context)

@login_required(login_url='login')
def add_client(request):
    client_form = AddClientForm()

    if request.method == 'POST':
        client_form = AddClientForm(request.POST, request.FILES)
        if client_form.is_valid():
            client_form.save()
            return redirect('clients')

    context = {
        'form': client_form,
    }
    return render(request, 'ctapp/add_client.html', context)

@login_required(login_url='login')
def add_transaction(request):
    transaction_form = AddTransactionForm()

    if request.method == 'POST':
        transaction_form = AddTransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction_form.save(commit=False)
            transaction_form.frm = request.user
            transaction_form.save()
            return redirect('transactions')

    context = {
        'form': transaction_form,
    }
    return render(request, 'ctapp/add_transaction.html', context)