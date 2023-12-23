from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
# Create your views here.
def index(request):
    entrants = entrant.objects.all()
    return render(request,'main/main_page.html',{'entrants':entrants})

def get_entrants_by_faculty(request):
    faculty_name = 'КТИ'
    entrants_on_faculty = entrant.objects.filter(faculty_id__name=faculty_name)
    return render(request,'main/faculty.html',{'entrants_on_faculty':entrants_on_faculty})

def marks(request):
    entrants_all = entrant.objects.all()
    entrants = []
    for abiturient in entrants_all:
        abiturient_dict = {'name': abiturient.name, 'group': abiturient.group_id, 'flow': abiturient.flow_id}
        abiturient_marks = mark.objects.filter(entrant_id=abiturient['id'])
        exam_id = []
        for el in abiturient_marks:
            exam_id.append(el.exam_id)
        abiturient_exams = exam.objects.filter(id__in=exam_id)
        abiturient_dict['marks'] = abiturient_marks
        abiturient_dict['exams'] = abiturient_exams
        entrants.append(abiturient_dict)

    return render(request, 'main/marks.html', {'entrants': entrants})


