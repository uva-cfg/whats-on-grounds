from django.shortcuts import render

# Create your views here.

def sign_up(request):
    return render(request, 'signup.html')

def sign_in(request):
    return render(request, 'signin.html')
