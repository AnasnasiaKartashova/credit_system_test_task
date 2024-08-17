from rest_framework import serializers
from credit_system.models import MakerModel


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakerModel
        fields = "__all__"
