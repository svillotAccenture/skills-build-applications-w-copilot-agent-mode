from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection

from bson.objectid import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        # For Djongo, get the native MongoDB client
        db = db.client['octofit_db']
        # Drop collections if they exist
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].drop()

        # Teams
        teams = [
            {'_id': ObjectId(), 'name': 'Team Marvel'},
            {'_id': ObjectId(), 'name': 'Team DC'},
        ]
        db['teams'].insert_many(teams)

        # Users
        users = [
            {'_id': ObjectId(), 'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': teams[0]['_id']},
            {'_id': ObjectId(), 'name': 'Captain America', 'email': 'cap@marvel.com', 'team': teams[0]['_id']},
            {'_id': ObjectId(), 'name': 'Batman', 'email': 'batman@dc.com', 'team': teams[1]['_id']},
            {'_id': ObjectId(), 'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': teams[1]['_id']},
        ]
        db['users'].insert_many(users)
        db['users'].create_index('email', unique=True)

        # Activities
        activities = [
            {'_id': ObjectId(), 'user': users[0]['_id'], 'type': 'run', 'distance': 5},
            {'_id': ObjectId(), 'user': users[1]['_id'], 'type': 'cycle', 'distance': 20},
            {'_id': ObjectId(), 'user': users[2]['_id'], 'type': 'swim', 'distance': 2},
            {'_id': ObjectId(), 'user': users[3]['_id'], 'type': 'run', 'distance': 10},
        ]
        db['activities'].insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'_id': ObjectId(), 'team': teams[0]['_id'], 'points': 100},
            {'_id': ObjectId(), 'team': teams[1]['_id'], 'points': 90},
        ]
        db['leaderboard'].insert_many(leaderboard)

        # Workouts
        workouts = [
            {'_id': ObjectId(), 'user': users[0]['_id'], 'workout': 'Pushups', 'reps': 30},
            {'_id': ObjectId(), 'user': users[1]['_id'], 'workout': 'Situps', 'reps': 40},
            {'_id': ObjectId(), 'user': users[2]['_id'], 'workout': 'Squats', 'reps': 50},
            {'_id': ObjectId(), 'user': users[3]['_id'], 'workout': 'Lunges', 'reps': 60},
        ]
        db['workouts'].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
