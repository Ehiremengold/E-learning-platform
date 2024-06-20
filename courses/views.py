from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.template.loader import render_to_string

from .models import Course, Category, CareerPath, Comment
from .forms import CourseForm, CareerPathForm, CommentForm
from django.contrib import messages
from django.db.models import Q
"""
create CRUD functions for Courses
"""


def course_by_category(request, category_slug):
    categories = Category.objects.all()
    course = Course.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        course = course.filter(category=category)[:3]
    context = {"categories": categories,
               "course": course,
               "category": category}
    return render(request, 'category.html', context)


@login_required
def retrieve_course_details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    interested_courses = Course.objects.filter(category=course.category)
    comments = Comment.objects.filter(course=course, reply=None).order_by('-timestamp')

    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = request.POST.get('chat')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(course=course, user=request.user, chat=comment, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {"course": course, "comments": comments, "form": form,
                                                  "interested_courses": interested_courses}
    return render(request, 'coursedetails.html', context)


def all_category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, 'categories.html', context)

@login_required
def question_users(request):
    form = CareerPathForm()
    if request.method == 'POST':
        form = CareerPathForm(request.POST or None)
        if form.is_valid():
            user_answer = form.save(commit=False)
            user_answer.user = request.user
            user_answer.save()
            return redirect('home')
        else:
            form = CareerPathForm()
    return render(request, 'question.html', {"form": form})


@login_required
def create_course(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            messages.success(request, 'Course created successfully!')
            return redirect('profile')
        else:
            form = CourseForm()
    context = {'form': form}
    return render(request, 'createcourse.html', context)



@login_required
def update_course(request, slug):
    context = {}
    obj = get_object_or_404(Course, slug=slug)
    form = CourseForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Course Updated Successfully!")
        return redirect("profile")
    context['form'] = form
    return render(request, 'updatecourse.html', context)


@login_required
def delete_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course Deleted Successfully!")
        return redirect("profile")
    return render(request, 'deletecourse.html', {})


def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        results = Course.objects.filter(Q(course_name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
        return render(request, 'search.html', {"results": results, "search": query})


def adminsearch(request):    
    if request.method == "GET":
        search = request.GET.get('q')
        results = Course.objects.filter(Q(course_name__icontains=search) | Q(description__icontains=search) | Q(category__name__icontains=search))
        return render(request, 'profile.html', {"results": results, "search": search})



