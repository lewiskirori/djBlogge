from django.shortcuts import render
from datetime import datetime
from operator import attrgetter
from blog.models import BlogPost
from blog.views import get_blog_queryset

def home_screen_view(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['search_query']
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts

    current_year = datetime.now().year
    context['current_year'] = current_year

    return render(request, "personal/home.htm", context)
