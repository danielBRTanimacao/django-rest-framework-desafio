from django.contrib import admin
from api.models import Student, StudentNote

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'register_number', 'school_serie',)
    list_display_links = ('id', 'name', 'register_number',)
    ordering = '-id',
    search_fields = ('id', 'name', 'register_number',)
    list_per_page = 10
    list_max_show_all = 150

@admin.register(StudentNote)
class StudentNotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'first_semester',)
    list_display_links = ('id', 'owner', 'first_semester',)
    ordering = '-id',
    search_fields = ('id', 'owner', )
    list_per_page = 10
    list_max_show_all = 150