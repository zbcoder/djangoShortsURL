from django.shortcuts import render

# Create your views here.

def myprofile(request):
    return render(request, 'profile/profile.html', context={'title': 'Личный кабинет'})