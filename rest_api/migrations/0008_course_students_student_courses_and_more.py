# Generated by Django 4.1 on 2023-03-15 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_alter_coursestudent_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='rest_api.CourseStudent', to='rest_api.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(through='rest_api.CourseStudent', to='rest_api.course'),
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.course'),
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.student'),
        ),
    ]