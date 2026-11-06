from django.shortcuts import render

def home(request):
    return render(request, 'form_app/home.html')
    
def about(request):
    return render(request, 'form_app/about.html')

def contact(request):
    return render(request, 'form_app/contact.html')

def form(request):
    name = ''
    email = ''
    if(request.method=="POST"):
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request, 'form_app/form.html', {"name":name, "email":email})
    else:
        return render(request, 'form_app/form.html', {"name":name, "email":email})