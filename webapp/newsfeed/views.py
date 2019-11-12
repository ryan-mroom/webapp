from django.shortcuts import render
from .models import Post
from django.forms.models import model_to_dict


def home(request):
    posts = [model_to_dict(Post.objects.all()[0])]

    for post in posts:
        post.update({'tags_array': get_tags(post)})

    context = {
        'title': 'Newsfeed',
        'posts': posts
    }
    return render(request, 'newsfeed/home.html', context)


def get_tags(post):
    return post['tags'].split(" ")