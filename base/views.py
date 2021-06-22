from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, 
    #FormView
)
from . models import Item
from . forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save()
            if user is not None:
                login(request, user)
                return redirect('home')

    form = RegisterForm()
    return render(request, 'base/register.html', {'form': form})


class TaskList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'tasks'
    template_name= 'base/index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tasks']= context['tasks'].filter(user= self.request.user)
        context['count']= context['tasks'].filter(complete=False).count()

        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']= context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input

        return context


class TaskView(LoginRequiredMixin, DetailView):
    model = Item

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['title', 'desc', 'complete' ]
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields= ['title', 'desc', 'complete' ]
    success_url= reverse_lazy('home')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url= reverse_lazy('home')


# below using FormView for User Register form.
'''class RegisterForm(FormView):
    template_name= 'base/register.html'
    form_class= UserCreationForm
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterForm, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterForm, self).get(*args, **kwargs)'''



   
    


