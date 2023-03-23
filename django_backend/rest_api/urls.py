from django.urls import path

from rest_api.views import CoursesByAvgStudentAge, \
    CoursesByNumberOfOtherCoursesEnrolledIn, \
    StudentCourseEnrollment, CourseListCreateView, \
    CourseDetailsUpdateDeleteView

urlpatterns = [

    path("courses/", CourseListCreateView.as_view()),
    path("courses/<int:pk>/", CourseDetailsUpdateDeleteView.as_view()),
    path("enroll/", StudentCourseEnrollment.as_view()),
    path("courses/by-avg-student-age/", CoursesByAvgStudentAge.as_view()),
    path("courses/by-other-courses-enrolled-in/", CoursesByNumberOfOtherCoursesEnrolledIn.as_view()),
]