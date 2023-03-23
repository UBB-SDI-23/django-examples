from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    courses = models.ManyToManyField('Course', through='CourseStudent')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='CourseStudent')

    def __str__(self):
        return self.name


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} - {self.student.name}"

