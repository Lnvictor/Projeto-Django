# from django.shortcuts import render
# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html', {'contato_email': "vh141299@gmail.com"})
