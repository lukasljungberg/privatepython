from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
import os
import markdown
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Note, PyUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = PyUser.objects.get(username=username)
        if not check_password(password, user.password):
            messages.error(request, "Invalid username or password")
        else:
            login(request, user)
            return redirect("index")  # Redirect to home/dashboard

    return render(request, "website/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif PyUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = PyUser.objects.create(username=username, password=make_password(password))
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")

    return render(request, "website/register.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def get_user_notes(request, user_id):
    user = get_object_or_404(User, id_hash=user_id)

    if request.user != user:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    notes = Note.objects.filter(user=user).values("module_name", "section_name", "content")
    return JsonResponse({"notes": list(notes)})

def index(request: HttpRequest):
    return render(request, 'website/index.html')

@login_required
def courses(request):
    return render(request, 'website/courses.html')
    
def ide(request):
    return render(request, 'website/run_code.html')

@login_required
def course(request: HttpRequest, course_name):
    sel_section = request.GET.get('section')

    if request.method == "POST":
        note_content = request.POST.get('note')
        user = PyUser.objects.get(username=request.user.username)
        # Then create a new note, associating it with that user
        Note.objects.create(
            user=user,  # Foreign key to the User
            module_name=course_name,
            section_name=sel_section,
            content=note_content
        )
        
        messages.success(request, "Saved note!")
        
    if course_name == "py_zero":
        sel_section = sel_section if sel_section else 'what_is_python'  
        sections = [{'title': 'What is Python?', 'uri': 'what_is_python'},
                    {'title': 'Terminology', 'uri': 'terminology'},
                    {'title': 'Syntax', 'uri': 'syntax'},
                    {'title': 'Data types', 'uri': 'data_types'},
                    {'title': 'Classes and Funcitons', 'uri': 'class_and_function'},
                    {'title': 'Is data type', 'uri': 'is_data_types'},
                    {'title': 'Python Standard Library Modules', 'uri': 'python_standard_library_modules'},
                   ]
    if course_name == "py_hero":
        sel_section = sel_section if sel_section else 'decorators'
        sections = [{'title': 'Decorators', 'uri': 'decorators'},
                    {'title': 'Threads', 'uri': 'threads'},
                    {'title': 'Events', 'uri': 'events'},
                    {'title': 'Queue', 'uri': 'queue'},
                    {'title': 'Signal', 'uri': 'signal'},
                    {'title': 'Advanced Python Libraries', 'uri': 'advanced_python_libraries'},
                   ]
    with open(os.path.join(settings.BASE_DIR, 'website', 'markdown', course_name, sel_section+'.md'), 'r') as f:
        md = f.read()
        html_content = markdown.markdown(md, extensions=['extra', 'nl2br', 'fenced_code', 'codehilite', 'tables', 'toc'])

    module = {'sections': sections, 'markdown': html_content, 'course': course_name, 'module': sel_section, 'notes': [x for x in request.user.user_notes.all().order_by("position") if x.section_name == sel_section], 'sel_section': sel_section}

    return render(request, 'website/course.html', module)

@csrf_exempt
@login_required
def update_note_order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        for item in data.get("notes", []):
            note = Note.objects.get(id=item["id"])
            note.position = item["position"]
            note.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

@csrf_exempt
@login_required
def delete_note(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id, user=request.user)
        note.delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

@login_required
def open_challenge(request: HttpRequest, course_name, section):
    with open(os.path.join(settings.BASE_DIR, 'website', 'challenges', course_name, section+'.py'), 'r') as f:
        challenge = f.read().split('# STATIC')[0]
    challenge = challenge.replace("USERNAME", request.user.username)
    return render(request, 'website/run_code.html', {'code': challenge, 'course_name': course_name, 'section': section})

@login_required
def check_challenge(request: HttpRequest, course_name, section, output):
    with open(os.path.join(settings.BASE_DIR, 'website', 'challenges', course_name, section+'.py'), 'r') as f:
        challenge = f.read().split('# STATIC')

    unchangeable = ""
    unchangeable = challenge[1].split("# Don't change")[1].strip()
    static_code = json.loads(request.body.decode())['code'].split("# Don't change")[1]
    for nr in static_code.splitlines():
        print(repr(nr))
        if str(nr).isdigit():
            static_code = static_code.replace(nr + '\n', "")

    static_code = static_code.replace('\u200b', '').replace('\n', '').strip()
    unchangeable = unchangeable.replace('\n', '').strip().replace('USERNAME', request.user.username)
    print(static_code)
    print(unchangeable)
    if static_code == unchangeable and output == "Hello " + request.user.username + "!":
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})