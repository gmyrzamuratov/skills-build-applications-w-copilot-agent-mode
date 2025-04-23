# Test data for populating octofit_db based on the MonaFit Tracker example
# This file will be imported by the management command

test_data = {
    "users": [
        {"email": "alice@example.com", "name": "Alice Octo", "password": "alicepass"},
        {"email": "bob@example.com", "name": "Bob Cat", "password": "bobpass"},
        {"email": "carol@example.com", "name": "Carol Ray", "password": "carolpass"}
    ],
    "teams": [
        {"name": "Octo Runners", "members": ["alice@example.com", "bob@example.com"]},
        {"name": "Fit Cats", "members": ["carol@example.com"]}
    ],
    "activity": [
        {"user_id": "alice@example.com", "type": "run", "duration": 30, "date": "2025-04-20"},
        {"user_id": "bob@example.com", "type": "walk", "duration": 45, "date": "2025-04-20"},
        {"user_id": "carol@example.com", "type": "strength", "duration": 20, "date": "2025-04-20"}
    ],
    "leaderboard": [
        {"team_id": "Octo Runners", "points": 150},
        {"team_id": "Fit Cats", "points": 80}
    ],
    "workouts": [
        {"user_id": "alice@example.com", "activity_type": "run", "details": "5km", "date": "2025-04-20"},
        {"user_id": "bob@example.com", "activity_type": "walk", "details": "3km", "date": "2025-04-20"},
        {"user_id": "carol@example.com", "activity_type": "strength", "details": "pushups", "date": "2025-04-20"}
    ]
}
