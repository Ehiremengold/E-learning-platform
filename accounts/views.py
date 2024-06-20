from .models import Account
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import (
                                  authenticate,
                                  logout,
                                  login
                              )
from django.shortcuts import (
                                  render,
                                  get_object_or_404,
                                  redirect
                              )
from .forms import (
                    RegistrationForm,
                    AccountAuthenticationForm,
                    AccountUpdateform
                )
from courses.models import CareerPath, Course, Category


def registration_view(request):
    """
      Renders Registration Form 
    """
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pass)
            messages.success(request, "Account Created!")
            return redirect('login')
        else:
            messages.warning(request, "Your credentials maybe invalid or in use!")
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("/")


def login_view(request):
    """
      Renders Login Form
    """
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In")
            if CareerPath.objects.filter(user=user).exists():
                return redirect("home")
            else:
                return redirect("question")
        else:
            messages.warning(request, "Login Failed: Your email or password is incorrect!")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, "login.html", context)


def update_account_view(request):
    """
      Update userprofile page "
    """
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.POST:
        form = AccountUpdateform(request.POST, instance=request.user)
        username = request.POST.get('username')
        email = request.POST.get('email')
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated")
        else:
            messages.error(request, "Please Correct Below Errors!")
    else:
        form = AccountUpdateform(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )
    context['account_form'] = form

    return render(request, "profile.html", context)


def profile_display(request):

    """
    Renders userprofile page
    omo contents to show?
    0. home
    1. username
    2. study hours
    3. started courses
    4. finished courses
    5. update account
    6. logout
    """
    if not request.user.is_authenticated:
        return redirect("login")
    user = request.user
    courses = Course.objects.all()
    user_qn = CareerPath.objects.get(user=user)
    recommended_courses = Category.objects.get(name=user_qn.choose_a_career_path[0]).category.all().order_by('-timestamp')[:3]
    context = {'user': user, 'courses': courses, 'user_qn': user_qn, 'recommended_courses': recommended_courses}
    return render(request, "profile.html", context)

