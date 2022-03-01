from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def withdraw(request):
    return render(request, 'pages/withdraw.html')

def deposit(request):
    return render(request, 'pages/deposit.html')

def bnb(request):
    return render(request, 'pages/bnb.html')

def btc(request):
    return render(request, 'pages/btc.html')

def eth(request):
    return render(request, 'pages/eth.html')

def sol(request):
    return render(request, 'pages/sol.html')

def usdt(request):
    return render(request, 'pages/usdt.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')
