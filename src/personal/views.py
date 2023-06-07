from django.shortcuts import render
from datetime import datetime
from operator import attrgetter
from blog.models import BlogPost

def home_screen_view(request):
    context = {}
    blog_posts = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts

    current_year = datetime.now().year
    context['current_year'] = current_year

    return render(request, "personal/home.htm", context)
