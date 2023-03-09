from django.db.models import Avg
from rest_framework import generics
from .models import Course, Student, Teacher, CourseStudent
from .serializers import CourseSerializer, StudentSerializer, \
    TeacherSerializer, CourseStudentSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentCourseEnrollment(generics.CreateAPIView):
    serializer_class = CourseStudentSerializer


class CoursesByAvgStudentAge(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        query = Course.objects\
            .annotate(avg_age=Avg('coursestudent__student__age'))\
            .order_by('avg_age')
        print(query.query)

        return query


class CoursesWithStudents(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        courses = CourseStudent.objects.select_related('course', 'student')
        print(courses.query)
        for course in courses:
            students = Course.objects.filter(id=course.id).values('coursestudent__student__name')
            print(students.query)
            for student in students:
                print(student)
