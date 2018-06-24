from django.http import HttpResponse
from django.template import loader
from .models import Course

def index(request):
    all_courses = Course.objects.all()
    html=''
    for course in all_courses:
        url = '/courses/' + str(course.id) + '/'
        html+= '<a href="' + url + '">' + course.name + '</a><br>'
    return HttpResponse(html)

def detail(request,course_id):
    zmienna = Course.objects.filter(id=course_id).first()
    return HttpResponse("<h2>Details for course id: " +  str(zmienna) +"</h2>")
