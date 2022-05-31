from rest_framework import serializers


class TeamSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False)
    name = serializers.CharField()
    flag_image = serializers.CharField()
    shield_image = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)


class UpdateTeamSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    flag_image = serializers.CharField(required=False)
    shield_image = serializers.CharField(required=False)
