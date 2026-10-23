from django.shortcuts import render

def about(request):
    return render(request,'templates_app/about.html')
def contact(request):
    return render(request,'templates_app/contact.html')
