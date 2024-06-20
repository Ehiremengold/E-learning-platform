from django.contrib.auth import get_user_model
from django.db import models
from quizes.models import Quiz
User = get_user_model()


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user} + {self.quiz} + {self.score}"
