# Generated by Django 4.1 on 2023-03-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_remove_course_students_coursestudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestudent',
            name='enrollment_date',
            field=models.DateField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
