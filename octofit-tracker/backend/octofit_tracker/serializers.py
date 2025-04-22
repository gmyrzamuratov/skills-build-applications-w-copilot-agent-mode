# Serializers for MongoDB collections using DRF's Serializer class
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # Add more fields as needed

class TeamSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()
    date = serializers.DateField()

class LeaderboardSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    team_id = serializers.CharField()
    points = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    activity_type = serializers.CharField()
    details = serializers.CharField()
    date = serializers.DateField()
