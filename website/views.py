from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the main page. Go to /courses to see our offer.</h1>")