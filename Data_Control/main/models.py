
from django.db import models

# Create your models here.
class entrant(models.Model):
    name = models.CharField('ФИО', max_length=50)
    group_id = models.ForeignKey('group', on_delete=models.PROTECT, default=1, verbose_name='Группа')
    flow_id = models.ForeignKey('flow', on_delete=models.PROTECT, default=1, verbose_name='Поток')
    faculty_id = models.ForeignKey('faculty', on_delete=models.PROTECT,default=1,verbose_name='ID факультета')
    department_id = models.ForeignKey('department', on_delete=models.PROTECT,default=1,verbose_name='ID кафедры')
    exam_list = models.PositiveIntegerField('Номер экзаменационного листа', default=0)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'

class faculty(models.Model):
    name = models.CharField('Название', max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

class department(models.Model):
    name = models.CharField('Название', max_length=100)
    faculty_id = models.ForeignKey('faculty', on_delete=models.PROTECT,default=1,verbose_name='ID факультета')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
class mark(models.Model):
    entrant_id = models.ForeignKey('entrant', on_delete=models.PROTECT, default=1, verbose_name='ID Абитуриента')
    exam_id = models.ForeignKey('exam', on_delete=models.PROTECT,default=1,verbose_name='ID экзамена')
    mark = models.PositiveSmallIntegerField('Оценка', default=0)
    def __str__(self):
        return f'{self.entrant_id.name}, предмет: {self.exam_id}'

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
class exam(models.Model):
    subject_id = models.ForeignKey('subject', on_delete=models.PROTECT, default=1, verbose_name='ID предмета')
    flow_id = models.ForeignKey('flow', on_delete=models.PROTECT, default=1, verbose_name='Поток')
    classroom = models.PositiveSmallIntegerField('Аудитория', default=0)
    exam_date = models.DateTimeField('Дата экзамена')
    consult_date = models.DateTimeField('Дата консультации')
    def __str__(self):
        return self.subject_id.name

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'
class subject(models.Model):
    name = models.CharField('Название', max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
class flow(models.Model):
    flow_num = models.PositiveIntegerField('Номер потока')
    def __str__(self):
        return str(self.flow_num)

    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'
class group(models.Model):
    group_num = models.PositiveIntegerField('Номер группы')
    flow_id = models.ForeignKey('flow', on_delete=models.PROTECT, default=1, verbose_name='Поток')
    def __str__(self):
        return str(self.group_num)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'