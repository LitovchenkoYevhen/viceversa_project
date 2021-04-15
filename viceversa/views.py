from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html', {'greeting':'Hello'})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    lenth = len(user_text)
    return render(request, 'reversed.html', {'usertext':user_text, 'reversedtext':reversed_text, 'lenth': lenth})