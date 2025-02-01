from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, you meeting Aditya")
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def profile(request):
    return render(request, 'website/profile.html')

def mine(request):
    return render(request, 'mine/all_mine.html')