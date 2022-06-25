from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from book.models import BookInfo
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views import View


def create_book(request):

    book = BookInfo.objects.create(
        name='aveee',
        pub_data='2000-1-1',
        readcount=10

    )

    return HttpResponse('create')


def shop(request, city_id, mobile):
    query_params = request.GET
    #print(query_params)
    order = query_params.getlist('order')
    #order = query_params['order']
    print(order)
    print(mobile)
    return HttpResponse('店铺')


def register(request):

    data = request.POST
    username = data.get['username']
    password = data.get['password']
    return HttpResponse('ok')


def json(request):

    body = request.body
    #print(type(body))
    body_str = body.decode()
    #print(body_str)
    # json形式的字符串转换为python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    print(request.META['SERVER_PORT'])
    return HttpResponse('ok')


def method(request):
    print(request.method)
    return HttpResponse('ok')


def response(request):
    info = [

        {'name':'yoki',
        'address':'nancang'},
    ]
    #data 返回的响应数据，一般是字典类型

    res = JsonResponse(data=info,safe=False)
    return redirect('http://www.baidu.com')


def set_cookie(request):
    username = request.GET.get("username")
    res = HttpResponse('set_cookie')

    res.set_cookie('name',username)

    return res


def get_cookie(request):

    name = request.COOKIES.get('name')
    print(request.COOKIES)


    return  HttpResponse(name)


def set_session(request):
    username = request.GET.get('username')
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse('set_session')


def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    content = '{},{}'.format(user_id,username)
    return HttpResponse(content)


class LoginView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')
