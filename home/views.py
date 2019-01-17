from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.views import View


# Create your views home here.

def home(request):
    return render(request, 'home.html')

#def menu(request):
    #return render(request, 'menu_principal.html')

def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'index2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variavel'] = 'Bionic-Techo-Info Me'
        return context

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'view.html')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
        
        