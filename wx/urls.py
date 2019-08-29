from django.urls import path
from wx import views

app_name = "wx"  # app应用命名空间 ,保证不会混淆
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index),
    path('login', views.login, name='login'),
    path('wxarticle', views.wxarticle, name='wxarticle'),
]