from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProflies(request, proflies, results):
    
    page = request.GET.get('page')
    paginator = Paginator(proflies, results)

    try:
        proflies = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        proflies = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        proflies = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    custom_range =  range(leftIndex, rightIndex)

    
    return custom_range, proflies

def searchProfiles(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query) | Q(skill__in=skills))

    return profiles, search_query