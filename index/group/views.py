from index.models import Group
from index.serializers import FlowSerializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from index.serializers import FlowSerializer
from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter


class GroupSerializer(serializers.ModelSerializer):
    constraints = serializers.JSONField()
    flow = FlowSerializer()

    class Meta:
        model = Group
        fields = '__all__'


class GroupFilter(FilterSet):
    code = CharFilter(field_name='code', lookup_expr='icontains')
    min_count_of_students = NumberFilter(field_name='count_of_students', lookup_expr='gte')
    max_count_of_students = NumberFilter(field_name='count_of_students', lookup_expr='lte')
    flow = CharFilter(field_name='flow', lookup_expr='name__icontains')

    class Meta:
        model = Group
        fields = {
            'code':['exact'],
            'min_count_of_students': ['exact'],
            'max_count_of_students': ['exact'],
            'flow': ['exact'],
        }


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()  
    serializer_class = GroupSerializer
    filterset_class = GroupFilter 