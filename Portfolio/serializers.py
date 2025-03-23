from Portfolio.models import Portfolio, Education, Projects
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

class PortfolioSerializer(ModelSerializer):
    education = serializers.PrimaryKeyRelatedField(many=True, queryset=Education.objects.all())
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Projects.objects.all())

    class Meta:
        model = Portfolio
        fields = ['title', 'tech_stack', 'description', 'social_link', 'intrests', 'education', 'projects']
        extra_kwargs={
            'social_link': {'required': False},
            'intrests': {'required': False},
        }

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['college', 'university', 'degree', 'field', 'cgpa', 'start_date', 'end_date']

class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'tech_stack', 'description', 'project_link', 'start_date', 'end_date']
        extra_kwargs={
            'project_link': {'required': False},
        }