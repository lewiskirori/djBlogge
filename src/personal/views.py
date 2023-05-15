from django.shortcuts import render
from datetime import datetime
from account.models import Account

def home_screen_view(request):
    context = {}

    accounts = Account.objects.all()
    context['accounts'] = accounts

    current_year = datetime.now().year
    context['current_year'] = current_year

    return render(request, "personal/home.htm", context)
