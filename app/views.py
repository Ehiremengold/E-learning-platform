from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, Http404
from courses.models import Course, CareerPath, Category
from django.contrib import messages


def landingpage(request):
    courses = Course.objects.all()[:4]
    return render(request, 'landingpage.html', {"courses": courses})

@login_required
def index(request):
    user = request.user
    courses = Course.objects.all()[:6]
    categories = Category.objects.all()[:6]
    user_qn = CareerPath.objects.get(user=user)
    just_updated = Course.objects.all().order_by('-timestamp')[:3]
    recommended_courses = Category.objects.get(name=user_qn.choose_a_career_path[0]).category.all().order_by('-timestamp')[:3]
    context = {"categories": categories,
               "courses": courses,
               "recommended_courses": recommended_courses,
               "just_updated": just_updated,
               }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {})

