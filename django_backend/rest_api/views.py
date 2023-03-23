from django.db.models import Avg, Count, OuterRef, Subquery, Q, Case, When, \
    IntegerField, Exists
from django.http import JsonResponse
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Student, Teacher, CourseStudent
from .serializers import CourseSerializer, StudentSerializer, \
    TeacherSerializer, CourseStudentSerializer


class CourseDetailsUpdateDeleteView(APIView):
    serializer_class = CourseSerializer

    def get(self, request, pk, *args, **kwargs):

        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, exclude_fields=['students__courses'])
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({'error': 'Course does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({'error': 'Course does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response({'message': 'Course deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({'error': 'Course does not exist'}, status=404)


class CourseListCreateView(APIView):
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True, exclude_fields=['students'])
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

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
