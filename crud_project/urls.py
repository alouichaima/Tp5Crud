from django.urls import path,include
from .views import BlogVieww, blogDeleteView, blogUpdateView, blogcreate
from django.views.generic.base import TemplateView
app_name="crud_project"
urlpatterns = [
    path('liste', BlogVieww.as_view(), name='blog_list'),  
    path('create',blogcreate.as_view(),name='createhtml'),
    path('update/<int:pk>',blogUpdateView.as_view(),name='updatehtml'),
    path('delete/<int:pk>',blogDeleteView.as_view(),name='deletehtml'),
]
