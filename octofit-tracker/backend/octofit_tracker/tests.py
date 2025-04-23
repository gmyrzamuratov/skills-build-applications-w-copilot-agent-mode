from django.test import TestCase
from rest_framework.test import APIClient
from pymongo import MongoClient

class OctofitAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.mongo = MongoClient('mongodb://localhost:27017/')
        self.db = self.mongo['octofit_db']
        self.db.users.delete_many({})
        self.db.teams.delete_many({})
        self.db.activity.delete_many({})
        self.db.leaderboard.delete_many({})
        self.db.workouts.delete_many({})

    def test_user_create(self):
        response = self.client.post('/users/', {'email': 'test@example.com', 'name': 'Test User', 'password': 'pass'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.db.users.count_documents({'email': 'test@example.com'}), 1)

    def test_team_create(self):
        response = self.client.post('/teams/', {'name': 'Team A', 'members': []}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.db.teams.count_documents({'name': 'Team A'}), 1)

    def test_activity_create(self):
        response = self.client.post('/activity/', {'user_id': '1', 'type': 'run', 'duration': 30, 'date': '2025-04-22'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.db.activity.count_documents({'type': 'run'}), 1)

    def test_leaderboard_create(self):
        response = self.client.post('/leaderboard/', {'team_id': '1', 'points': 100}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.db.leaderboard.count_documents({'team_id': '1'}), 1)

    def test_workout_create(self):
        response = self.client.post('/workouts/', {'user_id': '1', 'activity_type': 'run', 'details': '5km', 'date': '2025-04-22'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.db.workouts.count_documents({'activity_type': 'run'}), 1)
