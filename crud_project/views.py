from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from crud_project.models import BlogPost

# Create your views here.
class BlogVieww(ListView):
    model=BlogPost
    context_object_name='posts'
    template_name = "Posts/BlogView.html"  
    
class blogcreate(CreateView):
    model = BlogPost
    fields=['title','content','author','created_on']# soit fields soit form class
#form_class=blogform formulaire dans forms.py
    template_name = "Posts/BlogCreate.html"
    success_url=reverse_lazy('crud_project:blog_list')
    
    
class blogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author','content']
    pk_url_kwarg = 'pk'
    template_name = "Posts/update.html"
    success_url=reverse_lazy('Posts:blog_list')
    
class blogDeleteView(DeleteView):
    model = BlogPost
    pk_url_kwarg = 'pk'
    template_name = "Posts/delete.html"
    success_url=reverse_lazy('Posts:blog_list')
    

