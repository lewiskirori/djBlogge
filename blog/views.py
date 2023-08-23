from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponse
from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account

def create_blog_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    form =  CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
        context['success_message'] = 'Congrats! Your post has been published.'
    
    else:
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, "blog/create_blog.htm", context)


def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.htm', context)


def edit_blog_view(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")
    
    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse("Oops! Sorry, you are not authorized to perform this action. This action is restricted to the post’s author.")

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Masterpiece post was successfully updated!"
            blog_post = obj
            return redirect('blog:detail', slug=blog_post.slug)


    form = UpdateBlogPostForm (
        initial = {
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        } 
    )

    context['form'] = form
    return render(request, 'blog/edit_blog.htm', context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for search_query in queries:
        posts = BlogPost.objects.filter (
            Q(title__icontains=search_query) |
            Q(body__icontains=search_query)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list (set(queryset)) 