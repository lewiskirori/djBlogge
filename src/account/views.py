from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    current_year = datetime.now().year
    context['current_year'] = current_year
    return render(request, 'account/register.htm', context)


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if request.POST.get('remember_me'):
                    # Set a session cookie to remember the user's login for two weeks
                    request.session.set_expiry(60 * 60 * 24 * 14)  # 2 weeks
                # Redirect to the appropriate URL
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    current_year = datetime.now().year
    context['current_year'] = current_year

    return render(request, 'account/login.htm', context)
                    

def account_view(request):
    
    if not request.user.is_authenticated:
        return redirect("/login/?next={}&login=false&nis=false&".format(request.path))

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Account was updated"
    else:
        form = AccountUpdateForm(
            initial = {
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    current_year = datetime.now().year
    context['current_year'] = current_year
    return render(request, 'account/account.htm', context)


def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.htm', {})