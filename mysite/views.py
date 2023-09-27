from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.htm', status=404)

def custom_500(request):
    return render(request, '500.htm', status=500)
