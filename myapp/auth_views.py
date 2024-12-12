from django.shortcuts import render, redirect

def View_registerUser( request ):
    return render( request, 'auth/register.html')