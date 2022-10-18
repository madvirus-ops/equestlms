# Generated by Django 3.2.16 on 2022-10-16 19:30

import auto_prefetch
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('task', '0001_initial'),
        ('tutor', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='student_tutor_course', to='student.Student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='tasks',
            field=models.ManyToManyField(related_name='course_tasks', to='task.Task'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='tutor',
            field=auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_tutor_course', to='tutor.tutor'),
        ),
        migrations.AddField(
            model_name='course',
            name='tutors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_tutor', to='tutor.tutor'),
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together={('tutor', 'course')},
        ),
    ]
