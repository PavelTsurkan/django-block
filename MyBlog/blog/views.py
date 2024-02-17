from django.shortcuts import render
from blog.models import *


def index(request):
    context = {
        "posts": Post.objects.all() 
    }

    return render(
        request=request,
        context=context,
        template_name="blog/index.html"
    )