from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'page/main.html')

def mobile_view(request):
    return render(request, 'page/mobile.html')