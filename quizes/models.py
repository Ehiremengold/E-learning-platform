from django.db import models
import random
from courses.models import Course

DIFF_CHOICES = (('easy', 'easy'),
                ('medium', 'medium'),
                ('hard', 'hard'),)


class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="pass score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.course}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions
        # [:self.number_of_questions] displayed questions dependent on "number_of_questions".

    class Meta:
        verbose_name_plural = 'Quizes'
