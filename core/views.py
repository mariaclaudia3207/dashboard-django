# Create your views here.
# Visualização para renderizar a página html

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee

'''
class Index(View):
    template = 'index.html'
    
    def get(self, request):
        return render(request, self.template)
    

class Login(View):
    template = 'login.html'

    def get(self, request):
        return render(request, self.template)
'''

class Register(View):
    template = 'register.html'

    def get(self, request):
        return render(request, self.template)

class Base(View):
    template = 'base.html'

    def get(self, request):
        return render(request, self.template)

class Login(View):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})



class Index(LoginRequiredMixin, View):
    template = 'index.html'
    login_url = '/login/'

    #def get(self, request):
    #    return render(request, self.template)
        
        #aqui passa o banco e dados dos funcionários cadastrados para o arq. html xom um QuerySet
        
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, self.template, {'employees': employees})
        


