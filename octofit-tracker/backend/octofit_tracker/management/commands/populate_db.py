from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import test_data

class Command(BaseCommand):
    help = 'Populate octofit_db MongoDB with test data for users, teams, activity, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insert test data
        db.users.insert_many(test_data['users'])
        db.teams.insert_many(test_data['teams'])
        db.activity.insert_many(test_data['activity'])
        db.leaderboard.insert_many(test_data['leaderboard'])
        db.workouts.insert_many(test_data['workouts'])
        self.stdout.write(self.style.SUCCESS('Test data populated successfully in octofit_db.'))
