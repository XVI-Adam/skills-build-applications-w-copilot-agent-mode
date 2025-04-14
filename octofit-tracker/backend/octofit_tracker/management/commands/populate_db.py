from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "student1", "email": "student1@example.com", "password": "password1"},
            {"_id": ObjectId(), "username": "student2", "email": "student2@example.com", "password": "password2"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Team A", "members": [users[0]["_id"]]},
            {"_id": ObjectId(), "name": "Team B", "members": [users[1]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": timedelta(minutes=30)},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Cycling", "duration": timedelta(minutes=45)},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 150},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Morning Run", "description": "A quick morning run to start the day."},
            {"_id": ObjectId(), "name": "Evening Cycle", "description": "A relaxing evening cycling session."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
