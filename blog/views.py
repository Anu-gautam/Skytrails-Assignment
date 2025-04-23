from django.shortcuts import render, get_object_or_404
from .models import BlogPost
import requests

def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    countries = requests.get("https://restcountries.com/v3.1/all").json()[:5]
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'countries': countries})
