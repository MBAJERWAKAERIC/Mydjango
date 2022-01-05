from django.urls import path

from . import views

urlpatterns = [
    path('', views.Myapp, name='Myapp'),
]

from django.http import HttpResponse
def Myapp(request):
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))