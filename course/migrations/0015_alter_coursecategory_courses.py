# Generated by Django 3.2.16 on 2022-10-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_coursecategory_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.Course'),
        ),
    ]
