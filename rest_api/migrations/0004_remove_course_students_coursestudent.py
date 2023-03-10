# Generated by Django 4.1 on 2023-03-08 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_course_student_teacher_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.student')),
            ],
        ),
    ]
