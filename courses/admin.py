from django.contrib import admin
from .models import Course, Category, CareerPath, Comment


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'category', 'description', 'timestamp']
    search_fields = ['course_name']
    # prepopulated_fields = {'slug': ('course_name', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


admin.site.register(Course, CourseAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CareerPath)

