from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from autoslug import AutoSlugField
from multiselectfield import MultiSelectField
User = get_user_model()
"""
question1 = choose a career path: Web development, UI/UX/Graphic Design, Robotics, 
Microsoft Offices, Front Engineering, Backend Engineering, AI

question2 = have you had any previous IT knowledge?: YES, NO
question3 = Do you a github link? input here.: Charfield(max_length=255)

"""
question1choice = (("Software Development", "Software Development"),
                   ("UI/UX/Graphic Design", "UI/UX/Graphic Design"),
                   ("Robotics", "Robotics"),
                   ("Microsoft Offices", "Microsoft Offices"),
                   ("Cyber Security", "Cyber Security"),
                   ("Networking", "Networking"),
                   ("AI/Data Science/Machine Learning", "AI/Data Science/Machine Learning"),
                   )
question2choice = (("YES", "YES"),
                   ("NO", "NO"),
                   ("Not so Much", "Not so Much"))


class CareerPath(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """question1"""
    choose_a_career_path = MultiSelectField(choices=question1choice, max_length=3000)
    """question2"""
    have_you_had_any_previous_IT_knowledge = models.CharField(choices=question2choice, max_length=255)
    Github_link = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.user.username


CHOICE = (
    ("meets community guidelines", "Meets Community Guidelines"),
    ("withdraw course", "Withdraw Course")
)


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='category_thumnail')
    slug = AutoSlugField(populate_from='name', unique=True)
    about_category = models.TextField(max_length=20000)

    class Meta:
        ordering = ('-name', )
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    course_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='course_name', unique=True)
    file = models.FileField(upload_to='course_media/')
    description = models.TextField()
    course_thumbnail = models.ImageField(upload_to='course_thumbnail')
    external_links = models.CharField(max_length=255, null=True, blank=True)
    recommended_books = models.CharField(max_length=255, null=True, blank=True)
    requirements = models.TextField()
    choose = models.CharField(choices=CHOICE, max_length=255, default=1)
    total_course_time = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.course_name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    chat = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat


