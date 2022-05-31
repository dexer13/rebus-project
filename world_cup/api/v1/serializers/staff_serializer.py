from rest_framework import serializers


class StaffSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False)
    name = serializers.CharField()
    lastname = serializers.CharField()
    birth_date = serializers.DateField()
    team_id = serializers.IntegerField()
    nationality = serializers.CharField()
    rol = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)


class UpdateStaffSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    lastname = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    team_id = serializers.IntegerField(required=False)
    nationality = serializers.CharField(required=False)
    rol = serializers.CharField(required=False)
