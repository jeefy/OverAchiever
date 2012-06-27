import unittest
from OverAchiever.models import Achievement

class AchievementTestCase(unittest.TestCase):
    def setUp(self):
        self.Achievement = Achievement()
    def tearDown(self):
        self.Achievement.delete()
        self.Achievement = None
        