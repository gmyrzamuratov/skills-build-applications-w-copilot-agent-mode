from pymongo import MongoClient

# Connect to MongoDB (default connection string, adjust if needed)
client = MongoClient('mongodb://localhost:27017/')

db = client['octofit_db']

# Users collection: unique email, primary key _id
users = db['users']
users.create_index('email', unique=True)

# Teams collection
teams = db['teams']

# Activity collection
activity = db['activity']

# Leaderboard collection
leaderboard = db['leaderboard']

# Workouts collection
workouts = db['workouts']

# List collections
print(db.list_collection_names())
