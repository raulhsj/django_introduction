from django.http import HttpResponse, JsonResponse

from .forms import CreateNewProject, CreateNewTask
from .models import Project, Task
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):    
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

# def tasks(request, title):
def tasks(request):  
    # task = get_object_or_404(Task, id=id)
    # task = Task.objects.get(title=title)
    # return HttpResponse('task: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:        
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })