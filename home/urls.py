from django.urls import path
from .views import home, my_logout, HomePageView, MyView

from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    # Todo: pagina index em construção
    path('index/',TemplateView.as_view(template_name='index.html')),
    path('index2/', HomePageView.as_view(template_name='index2.html')),
    path('view/', MyView.as_view()),
    path('logout/', my_logout, name='logout'),
    
]