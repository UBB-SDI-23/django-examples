from django.urls import path

from rest_api.views import CourseList, CourseDetail, StudentList, \
    StudentDetail, TeacherList, TeacherDetail, StudentCourseEnrollment, \
    CoursesByAvgStudentAge, CoursesByNumberOfOtherCoursesEnrolledIn

urlpatterns = [
    path("courses/", CourseList.as_view()),
    path("courses/<int:pk>/", CourseDetail.as_view()),
    path("students/", StudentList.as_view()),
    path("students/<int:pk>/", StudentDetail.as_view()),
    path("teachers/", TeacherList.as_view()),
    path("teachers/<int:pk>/", TeacherDetail.as_view()),
    path("enroll/", StudentCourseEnrollment.as_view()),
    path("courses/by-avg-student-age/", CoursesByAvgStudentAge.as_view()),
    path("courses/by-other-courses-enrolled-in/", CoursesByNumberOfOtherCoursesEnrolledIn.as_view()),
]