from django.contrib import admin
from api.models import Course, Assessment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url',)
    list_display_links = ('id', 'title',)
    ordering = '-id',
    search_fields = ('id', 'title',)
    list_per_page = 10
    list_max_show_all = 150

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'email',)
    list_display_links = ('id', 'course', 'name',)
    ordering = '-id',
    search_fields = ('id', 'course', 'name',)
    list_per_page = 10
    list_max_show_all = 150