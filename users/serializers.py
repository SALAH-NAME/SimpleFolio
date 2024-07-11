from rest_framework import serializers
from .models import User, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'image', 'url', 'details']

class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        projects_data = validated_data.pop('projects')
        user = User.objects.create(**validated_data)
        for project_data in projects_data:
            Project.objects.create(user=user, **project_data)
        return user
