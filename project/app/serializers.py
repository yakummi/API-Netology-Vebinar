from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']

class NoteSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'user', 'text', 'is_private']
        read_only_fields = ['user']

    def validate_is_private(self, value):
        user = self.context['request'].user
        if value is True and Note.objects.filter(is_private=True, user=user).count() > 10:
            raise ValidationError('Слишком много секретов')

        return value
