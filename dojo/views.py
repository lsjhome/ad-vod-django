# dojo/views.py
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def mysum(request, numbers):
    # numbers = "1/2/12/123/12312/312/123123"
    result = sum(list(map(lambda s: int(s or 0), numbers.split("/"))))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message' : '안녕, 파이썬&장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
         }, json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    # filepath = '/home/jin009/projects/ask_django/django_basic/vod-django/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # 'text/html' 이 기본
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
