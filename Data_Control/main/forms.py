from django.forms import ModelForm, CharField, DateTimeField, Form

class GroupForm(Form):
    room_number = CharField(max_length=50,label='Номер')
    time = DateTimeField(label='Время')

