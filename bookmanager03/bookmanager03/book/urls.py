from django.urls import path

from book.views import create_book

from book.views import shop,register,json,method,response

from book.views import set_cookie,get_cookie,set_session,get_session
from django.urls import converters
from book.views import LoginView
from django.urls.converters import register_converter

class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     return value

register_converter(MobileConverter,'phone')
urlpatterns = [

    path('create/', create_book),
    path('<int:city_id>/<phone:mobile>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('response/', response),
    path('cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),

    path('order/',LoginView.as_view())
]