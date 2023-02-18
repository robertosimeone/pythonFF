from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate


# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created!')
#             return render(request, 'login.html')
#     else:
#         form = SignUpForm()
#     return render(request, 'login.html')
def login(request):
    return render(request,'login.html',{})
def logout_user(request):
    pass
def home(request):
    return render(request,'home.html',{})
