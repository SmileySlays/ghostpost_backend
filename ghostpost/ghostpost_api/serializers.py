from ghostpost.ghostpost_api.models import GhostPost
from rest_framework import serializers


class GhostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhostPost
        fields = ['body', 'likes', 'dislikes', 'boast', 'created_date']