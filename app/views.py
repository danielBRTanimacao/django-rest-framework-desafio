from django.shortcuts import render

from api.models import StudentNote

# Create your views here.
def index(request):
    student = StudentNote.objects.all()
    context = {
        'infos_student': student
    }
    return render(request, 'index.html', context)