from unittest import TestCase
from unittest.mock import MagicMock

from main import CookieParser


class TestCookieParser(TestCase):

    def test_single_active_cookie(self):
        cookie_parser = CookieParser('tests', 'test_single.csv', '2018-12-09')
        result = cookie_parser.get_cookie_by_date()
        self.assertIn('AtY0laUfhglK3lC7', result)

    def test_multiple_active_cookie(self):
        cookie_parser = CookieParser('tests', 'test_multiple.csv', '2018-12-08')
        result = cookie_parser.get_cookie_by_date()
        self.assertListEqual(['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA'], result)
