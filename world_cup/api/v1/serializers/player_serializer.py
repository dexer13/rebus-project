from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False)
    name = serializers.CharField()
    lastname = serializers.CharField()
    birth_date = serializers.DateField()
    team_id = serializers.IntegerField()
    photo = serializers.CharField()
    position = serializers.CharField()
    player_number = serializers.IntegerField()
    is_first_team = serializers.BooleanField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)


class UpdatePlayerSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    lastname = serializers.CharField(required=False)
    birth_date = serializers.DateField(required=False)
    team_id = serializers.IntegerField(required=False)
    photo = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    player_number = serializers.IntegerField(required=False)
    is_first_team = serializers.BooleanField(required=False)
