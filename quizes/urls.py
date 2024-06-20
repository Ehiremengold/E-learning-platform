from django.urls import path
from .views import (
    quiz_list_view,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
)


urlpatterns = [
    path('', quiz_list_view, name='allquizes'),
    path('<pk>/', quiz_view, name='quizpage'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
]
