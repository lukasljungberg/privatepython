from django.shortcuts import render
from django.conf import settings
import os
import markdown

def index(request):
    return render(request, 'website/index.html')

def courses(request):
    return render(request, 'website/courses.html')

def ide(request):
    return render(request, 'website/IDE.html')

def course(request, course_name):
    # temp module
    if course_name == "py_zero":
        sections = [{'title': 'What is Python?', 'uri': 'what_is_python', 'module': 'py_zero'}]
    for section in sections:
        with open(os.path.join(settings.BASE_DIR, 'website', 'markdown', section['module'], section['uri']+'.md'), 'r') as f:
            md = f.read()
            html_content = markdown.markdown(md, extensions=['nl2br'])
    module = {'sections': sections, 'markdown': html_content}

    return render(request, 'website/course.html', module)