from django.http import HttpResponse
from django.shortcuts import render
from . import models

def hello_world(request):
    return HttpResponse("Hello World")

def med_blog_all(request):
    post = models.Medicine_Post.objects.all()
    return render(request, 'medical_post_list.html', {'med_post': post})