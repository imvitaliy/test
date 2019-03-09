from rest_framework import serializers
from .models import Sentence


class SentenceSerializer(serializers.Serializer):
    title = serializers.CharField()
    sentence = serializers.CharField()

    class Meta(object):
        """Meta options."""
        model = Sentence
        fields = (
            'title',
            'sentence'
        )

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Sentence.objects.create(**validated_data)