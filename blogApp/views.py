from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import BlogModel


# function that calls my models to inject into the html and renders to the indexpage
def index(request):
    blog_list = BlogModel.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'blogApp/index.html', context)

# function that filters it by the Foreign Key
def myBlogs(request):
    blog_list = BlogModel.objects.filter(userName=request.user)
    context = {'blog_list': blog_list}
    return render(request, 'blogApp/myBlogs.html',context)
