from rest_framework import serializers

from rest_api.models import Course, Student, Teacher, CourseStudent


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    teacher_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    students = StudentSerializer(many=True, read_only=True)
    teacher = TeacherSerializer(read_only=True)

    avg_age = serializers.FloatField(read_only=True)

    def validate_teacher_id(self, value):
        filter = Teacher.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Teacher does not exist")
        return value

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'teacher_id', 'teacher', 'students', 'avg_age')


class CourseStudentSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)
    student_id = serializers.IntegerField(write_only=True)

    def validate_course_id(self, value):
        filter = Course.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Course does not exist")
        return value

    def validate_student_id(self, value):
        filter = Student.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Student does not exist")
        return value

    class Meta:
        model = CourseStudent
        fields = ('course_id', 'student_id')