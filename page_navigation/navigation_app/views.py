from django.shortcuts import render

def home(request):
    return render(request,'navigation_app/home.html')
def about(request):
    return render(request,'navigation_app/about.html')
def contact(request):
    return render(request,'navigation_app/contact.html')
def help(request):
    return render(request,'navigation_app/help.html')

