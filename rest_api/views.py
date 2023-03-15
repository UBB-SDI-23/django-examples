from django.db.models import Avg, Count, OuterRef, Subquery, Q, Case, When, \
    IntegerField, Exists
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
            .annotate(avg_age=Avg('enrolled_students__student__age'))\
            .order_by('avg_age')
        print(query.query)

        return query


class CoursesByNumberOfOtherCoursesEnrolledIn(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):

        query = Course.objects.annotate(
            num_other_courses=Count(
                Student.courses.through.objects.filter(
                    course_id=OuterRef('pk')
                ).exclude(
                    student_id=OuterRef('students__id')
                ).values('student_id').distinct(),
                distinct=True
            )
        ).order_by('-num_other_courses')

        print(query.query)

        return query
