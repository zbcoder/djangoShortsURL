from django.shortcuts import render, redirect
from .models import *
import json
from django.core import serializers
# Create your views here.

def myprofile(request):
    return render(request, 'profile/profile.html', context={'title': 'Личный кабинет'})


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
        print(request.user.id)
        data = json.loads(serializers.serialize('json', Links.objects.filter(user_id = request.user.id)))
        try:
            for record in data:
                print(record['fields']['cut_url'].split('/')[-2], cut_url)
                if record['fields']['cut_url'].split('/')[-2] == cut_url:
                    errors = 'Такая сокращенная ссылка уже существует! Введите другую'
                    return render(request, template_name='profile/links.html', context={'user_links': data, 'errors': errors, 'full_url': full_url})
            Links.objects.create(
                full_url = full_url,
                cut_url = '/link/'+cut_url+'/',
                user_id = User.objects.get(pk=request.user.id).id
            ).save()
            return redirect('create_link')
        except:
            pass
            
        
    