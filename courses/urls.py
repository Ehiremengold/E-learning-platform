from django.urls import path
from .views import search, create_course, question_users, retrieve_course_details, course_by_category, update_course, delete_course


urlpatterns = [
    path('know-user-recc/', question_users, name='question'),
    path('categories/<str:category_slug>/', course_by_category, name='category'),
    path('course/<str:slug>/', retrieve_course_details, name='coursedetails'),
    path('create-course/', create_course, name='createcourse'),
    path('update-course/<str:slug>/', update_course, name='updatecourse'),
    path('delete-course/<str:slug>/', delete_course, name='deletecourse'),
    path('search/', search, name='search'),
]