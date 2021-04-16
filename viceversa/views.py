from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html', {'greeting':'Hello'})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    counter_of_letters = 0
    for letter in user_text:
        if letter != ' ':
            counter_of_letters += 1
    words = len(user_text.split())
    return render(request, 'reversed.html', {'usertext':user_text, 'reversedtext':reversed_text, 'lenth': counter_of_letters, 'words':words})