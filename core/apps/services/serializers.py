from rest_framework import serializers
from core.apps.app.models import Todo
from django.utils import timezone

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'completed'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        todo = Todo.objects.create(**validated_data)
        return todo
        
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.updated_date = timezone.now()
        instance.updated_by = self.context['request'].user
        instance.save()

        return instance

    