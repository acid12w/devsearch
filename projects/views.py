from django.shortcuts import render, redirect
from .models import Project, Tag
from django.contrib import messages
from .form import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searcgProjects, paginateProjects

# Create your views here.

def projects(request):
    projects,  search_query= searcgProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context = {'projects': projects, 'search_query': search_query,'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)  

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'your review was successfully added')
        return redirect('project', pk=projectObj.id)


    return render(request, 'projects/single-project.html', {'project': projectObj, 'tag': tags,'form': form})

@login_required(login_url='login')
def createProject(request):
    profile =  request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            project = form.save(commit=False)
            print('Project:',form)  
            project.owner = profile  
            project.save()
            return redirect("account") 

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("account")

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)
