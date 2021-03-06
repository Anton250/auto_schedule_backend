from index.models import Teacher, Discipline, TeacherDetails
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import FilterSet, CharFilter
from index.lesson.views import SpecDisciplineSerializer
from django.db.models import Q


class TeacherSerializer(serializers.ModelSerializer):
    disciplines = SpecDisciplineSerializer(many=True, read_only=True)
    constraints = serializers.JSONField(required=False)
    disciplines_ids = serializers.ListField(write_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'disciplines', 'constraints', 'total_hours', 'disciplines_ids']


class TeacherFilter(FilterSet):
    name = CharFilter(field_name='first_name', method='filter_name')
    
    def filter_name(self, queryset, name, value):
        values = value.split(',')
        q = Q()
        for val in values:
            q |= Q(first_name__icontains=val)
            q |= Q(last_name__icontains=val)
            q |= Q(middle_name__icontains=val)
        return queryset.filter(q)

    class Meta:
        model = Teacher
        fields = {
            'name': ['exact',],
            'disciplines': ['exact'],
        }

        
class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    filterset_class = TeacherFilter

    def create(self, request):
        data = TeacherSerializer(data=request.data)

        data.is_valid(raise_exception=True)

        disciplines_ids = data.validated_data.pop('disciplines_ids', [])

        data.save()

        teacher = data.instance

        details = [
            TeacherDetails(teacher=teacher,
            discipline_id=discipline_id)
            for discipline_id in disciplines_ids
        ]

        TeacherDetails.objects.bulk_create(details)

        return Response(TeacherSerializer(instance=teacher).data, status=201)

    
    def update(self, request, pk=None):
        teacher = Teacher.objects.get(pk=pk)

        data = TeacherSerializer(data=request.data, instance=teacher)

        data.is_valid(raise_exception=True)

        disciplines_ids = data.validated_data.pop('disciplines_ids', [])

        data.save()

        teacher.details.all().delete()

        details = [
            TeacherDetails(teacher=teacher,
            discipline_id=discipline_id)
            for discipline_id in disciplines_ids
        ]

        TeacherDetails.objects.bulk_create(details)

        return Response(TeacherSerializer(instance=teacher).data)
