# Generated by Django 3.2.23 on 2023-12-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='faculty_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.faculty', verbose_name='ID факультета'),
        ),
        migrations.AlterField(
            model_name='entrant',
            name='faculty_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.faculty', verbose_name='ID факультета'),
        ),
    ]
