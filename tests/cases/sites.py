import unittest
from OverAchiever.models import Site

class SiteTestCase(unittest.TestCase):
    def setUp(self):
        self.Site = Site()
    def tearDown(self):
        self.Site.delete()
        self.Site = None
        