from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_index, name='index'),
    path('about', views.my_about, name='about'),
    path('add/<int:a>/<int:b>', views.add, name='add'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
    ]
