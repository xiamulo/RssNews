from django.urls import path
from wx import views
urlpatterns = [
    path('',views.index,name='index'),
]