from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', distance=5)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=10)
        self.workout = Workout.objects.create(user=self.user, workout='Pushups', reps=20)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 10)

    def test_workout(self):
        self.assertEqual(self.workout.reps, 20)
