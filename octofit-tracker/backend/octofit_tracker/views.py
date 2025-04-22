from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activity': '/activity/',
        'leaderboard': '/leaderboard/',
        'workouts': '/workouts/',
    })

# User Views
class UserList(APIView):
    def get(self, request):
        users = list(db.users.find())
        for user in users:
            user['_id'] = str(user['_id'])
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            db.users.insert_one(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        user = db.users.find_one({'_id': ObjectId(pk)})
        if not user:
            raise Http404
        user['_id'] = str(user['_id'])
        return user
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request, pk):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            db.users.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        db.users.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

# Team Views
class TeamList(APIView):
    def get(self, request):
        teams = list(db.teams.find())
        for team in teams:
            team['_id'] = str(team['_id'])
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            db.teams.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    def get_object(self, pk):
        team = db.teams.find_one({'_id': ObjectId(pk)})
        if not team:
            raise Http404
        team['_id'] = str(team['_id'])
        return team
    def get(self, request, pk):
        team = self.get_object(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    def put(self, request, pk):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            db.teams.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        db.teams.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

# Activity Views
class ActivityList(APIView):
    def get(self, request):
        activities = list(db.activity.find())
        for activity in activities:
            activity['_id'] = str(activity['_id'])
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            db.activity.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetail(APIView):
    def get_object(self, pk):
        activity = db.activity.find_one({'_id': ObjectId(pk)})
        if not activity:
            raise Http404
        activity['_id'] = str(activity['_id'])
        return activity
    def get(self, request, pk):
        activity = self.get_object(pk)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    def put(self, request, pk):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            db.activity.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        db.activity.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

# Leaderboard Views
class LeaderboardList(APIView):
    def get(self, request):
        leaderboard = list(db.leaderboard.find())
        for entry in leaderboard:
            entry['_id'] = str(entry['_id'])
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            db.leaderboard.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardDetail(APIView):
    def get_object(self, pk):
        entry = db.leaderboard.find_one({'_id': ObjectId(pk)})
        if not entry:
            raise Http404
        entry['_id'] = str(entry['_id'])
        return entry
    def get(self, request, pk):
        entry = self.get_object(pk)
        serializer = LeaderboardSerializer(entry)
        return Response(serializer.data)
    def put(self, request, pk):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            db.leaderboard.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        db.leaderboard.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

# Workout Views
class WorkoutList(APIView):
    def get(self, request):
        workouts = list(db.workouts.find())
        for workout in workouts:
            workout['_id'] = str(workout['_id'])
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            db.workouts.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    def get_object(self, pk):
        workout = db.workouts.find_one({'_id': ObjectId(pk)})
        if not workout:
            raise Http404
        workout['_id'] = str(workout['_id'])
        return workout
    def get(self, request, pk):
        workout = self.get_object(pk)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)
    def put(self, request, pk):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            db.workouts.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        db.workouts.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)
