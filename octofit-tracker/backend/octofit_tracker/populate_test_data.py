import sys
import os
from pymongo import MongoClient
    
# Ensure the parent directory is in sys.path for import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from octofit_tracker.test_data import test_data
except Exception as e:
    print('Failed to import test_data:', e)
    sys.exit(1)

try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['octofit_db']
    # Clear existing data
    for collection in ['users', 'teams', 'activity', 'leaderboard', 'workouts']:
        db[collection].delete_many({})
    # Insert test data
    db.users.insert_many(test_data['users'])
    db.teams.insert_many(test_data['teams'])
    db.activity.insert_many(test_data['activity'])
    db.leaderboard.insert_many(test_data['leaderboard'])
    db.workouts.insert_many(test_data['workouts'])
    print('Test data populated successfully in octofit_db.')
except Exception as e:
    print('Failed to populate test data:', e)
    sys.exit(1)
