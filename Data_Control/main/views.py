from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
from django.db.models import Q, Count
from datetime import timedelta
from .forms import GroupForm
# Create your views here.
def index(request):
    entrants = entrant.objects.all()
    return render(request,'main/main_page.html',{'entrants':entrants})

def get_entrants_by_faculty(request):
    faculty_name = faculty.objects.all()
    entrants_on_faculty = []
    for el in faculty_name:
        dict = {}
        names = entrant.objects.filter(faculty_id__name=el)
        dict[el] = names
        entrants_on_faculty.append(dict)
    return render(request,'main/faculty.html',{'entrants_on_faculty':entrants_on_faculty})
class get_certificate(DetailView):
    model = entrant
    template_name = 'main/certificate.html'
    context_object_name = 'entrant'
def marks(request):
    entrants_all = entrant.objects.all()
    entrants = []
    for abiturient in entrants_all:
        abiturient_dict = {'name': abiturient.name, 'group': abiturient.group_id, 'flow': abiturient.flow_id}
        abiturient_marks = mark.objects.filter(entrant_id=abiturient.id)
        exam_id = []
        for el in abiturient_marks:
            exam_id.append(el.exam_id.id)
        abiturient_exams = exam.objects.filter(id__in=exam_id)
        abiturient_dict['marks'] = abiturient_marks
        abiturient_dict['exams'] = abiturient_exams

        entrants.append(abiturient_dict)

    return render(request, 'main/marks.html', {'entrants': entrants})

def classrooms(request):
    groups = group.objects.all()
    classrooms = []
    for el in groups:
        classroom = []
        the_exam = exam.objects.filter(flow_id=el.flow_id.id)
        for exam_instance in the_exam:
            room = exam_instance.classroom
            classroom.append(room)
        classrooms.append({'group': el, 'exam': the_exam, 'room':classroom})
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            room_number = form.cleaned_data['room_number']
            time = form.cleaned_data['time']
            time_plus_2_hours = time + timedelta(hours=2)
            groups_all = group.objects.all()
            groups = []
            for el in groups_all:
                exams = exam.objects.filter(flow_id=el.flow_id.id).filter(classroom=room_number).filter(
                    Q(exam_date__gt=time, exam_date__lt=time_plus_2_hours) |
                    Q(consult_date__gt=time, consult_date__lt=time_plus_2_hours))
                if len(exams) > 0:
                    groups.append({'group': el, 'exam_date': exams})
            return render(request, 'main/classrooms.html', {'classrooms': classrooms,'groups': groups, 'form': form})
    else:
        form = GroupForm()
    groups = []
    return render(request, 'main/classrooms.html', {'classrooms': classrooms,'groups': groups, 'form': form})

def get_report(request):
    department_name = department.objects.all()
    group_name = group.objects.all()
    exam_name = exam.objects.all()
    subject_name = subject.objects.all()
    result = []
    count_depart = {}
    for el in department_name:
        count = entrant.objects.filter(department_id__name=el).count()
        count_depart[el] = count
    count_group ={}
    for el in group_name:
        count = entrant.objects.filter(group_id=el).count()
        count_group[el] = count
    exam_info ={}
    for el in exam_name:
        if el.subject_id not in exam_info.keys():
            date =[]
            places =[]
            date.append(el.exam_date)
            places.append(el.classroom)
            exam_info[el.subject_id] = [date,places]
        else:
            date = exam_info[el.subject_id][0]
            places = exam_info[el.subject_id][1]
            date.append(el.exam_date)
            places.append(el.classroom)
            exam_info[el.subject_id] = [date, places]
    marks_info = {}
    for mark_num in range(2, 6):

        marks = mark.objects.values('exam_id').annotate(count=Count('id')).filter(mark=mark_num)
        subjects_marks = {}
        for el in marks:
            exam_subject = exam.objects.get(id=el['exam_id'])
            if exam_subject.subject_id not in subjects_marks.keys():
                subjects_marks[exam_subject.subject_id] = el['count']
            else:
                subjects_marks[exam_subject.subject_id] += el['count']
        marks_info[mark_num] = subjects_marks
    result =[count_depart,count_group,exam_info,marks_info]
    return render(request, 'main/report.html', {'report': result})

