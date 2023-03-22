from rest_framework import serializers

from rest_api.models import Course, Student, Teacher, CourseStudent


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        kwargs.pop('fields', None)
        include_fields = kwargs.pop('include_fields', None)
        exclude_fields = kwargs.pop('exclude_fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if include_fields is not None:
            for field in include_fields:
                self.fields.append(field)
        if exclude_fields is not None:
            for field in exclude_fields:
                split = field.split('__')
                to_access = self.fields
                for i in range(len(split)-1):
                    to_access = to_access.get(split[i])
                if isinstance(to_access, serializers.ListSerializer):
                    to_access = to_access.child
                to_access.fields.pop(split[-1])


class TeacherSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(DynamicFieldsModelSerializer):
    teacher_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    teacher = TeacherSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)
    avg_age = serializers.FloatField(read_only=True)
    num_other_courses = serializers.IntegerField(read_only=True)

    def validate_teacher_id(self, value):
        filter = Teacher.objects.filter(id=value)
        if not filter.exists():
            raise serializers.ValidationError("Teacher does not exist")
        return value

    class Meta:
        model = Course
        fields = (
        'id', 'name', 'description', 'teacher_id', 'teacher', 'avg_age',
        'num_other_courses', 'students')


class CourseStudentSerializer(DynamicFieldsModelSerializer):
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
