from django.shortcuts import render, redirect
from .models import *
import json
from django.core import serializers
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def myprofile(request):
    if request.method == 'GET':
        form = CustomUserChangeForm()
    else:
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Информация успешно изменена!')
            return redirect('profile')
    return render(request, 'profile/profile.html', context={'title': 'Личный кабинет', 'form': form})
        
    
@login_required
def create_link(request):
    qs = Links.objects.filter(user_id = request.user.id)
    data = serializers.serialize('json', qs)
    if request.method=='GET':
        return render(request, template_name='profile/links.html', context={
            'title':'Создание коротких ссылок',
            'user_links': json.loads(data)
            })
    else:
        full_url = request.POST.get('full_url')
        cut_url = request.POST.get('cut_url')
        if cut_url[-1]=='/':
            cut_url = '/link/'+cut_url[0: -1]+'/'
        else:
            cut_url = '/link/'+cut_url+'/'
        data = json.loads(serializers.serialize('json', Links.objects.filter(user_id = request.user.id)))
        try:
            for record in data:
                if record['fields']['cut_url'] == cut_url:
                    errors = 'Такая сокращенная ссылка уже существует! Введите другую'
                    return render(request, template_name='profile/links.html', context={'user_links': data, 'errors': errors, 'full_url': full_url})
            Links.objects.create(
                full_url = full_url,
                cut_url = cut_url,
                user_id = User.objects.get(pk=request.user.id).id
            ).save()
            return redirect('create_link')
        except:
            pass


def home(request):
    return render(request, 'common_templates/home.html', context={'title':'Главная'})


def about(request):
    return render(request, 'common_templates/about.html', context={'title': 'Про нас'})
        
    