from .models import Course, CareerPath, Comment
from django import forms


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['course_name', 'file', 'description','course_thumbnail', 'requirements', 'total_course_time', 'external_links', 'category']


class CareerPathForm(forms.ModelForm):

    class Meta:
        model = CareerPath
        fields = ["choose_a_career_path", "have_you_had_any_previous_IT_knowledge", "Github_link"]
        widgets = {
            'choose_a_career_path': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'have_you_had_any_previous_IT_knowledge': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    chat = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))

    class Meta:
        model = Comment
        fields = ['chat']

