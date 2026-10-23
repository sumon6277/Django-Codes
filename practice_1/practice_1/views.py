from django.http import HttpResponse

def about(request):
    return HttpResponse("This is about page from practice web")

def contact(request):
    return HttpResponse("This is contact page from practice web")