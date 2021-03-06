from index.models import EducationPlan
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import FilterSet, CharFilter
from index.lesson.views import SpecDisciplineSerializer, SpecGroupSerializer


class EducationPlanSerializer(serializers.ModelSerializer):
    discipline = SpecDisciplineSerializer(read_only=True)
    group = SpecGroupSerializer(read_only=True)
    group_id = serializers.IntegerField(write_only=True)
    discipline_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = EducationPlan
        fields = '__all__'


class EducationPlanFilter(FilterSet):
    discipline = CharFilter(field_name='discipline', lookup_expr='title__icontains')
    group = CharFilter(field_name='group', lookup_expr='code__icontains')

    class Meta:
        model = EducationPlan
        fields = {
            'discipline':['exact'],
            'group': ['exact'],
        }

        
class EducationPlanViewSet(viewsets.ModelViewSet):
    queryset = EducationPlan.objects.all()
    serializer_class = EducationPlanSerializer
    filterset_class = EducationPlanFilter
