from rest_framework import serializers
from .models import Sentence


class SentenceSerializer(serializers.Serializer):
    title = serializers.CharField()
    sentence = serializers.CharField()
    created_at = serializers.DateTimeField()
    modified_at = serializers.DateTimeField()

    class Meta(object):
        """Meta options."""
        model = Sentence
        fields = (
            'title',
            'sentence',
            'created_at',
            'modified_at',
        )