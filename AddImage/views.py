from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render_to_response


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'addimage/post_list.html', {'posts': posts})

def kategorie(request, parameter):
    kategorie = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'addimage/kategorie.html', {'posts': kategorie})

