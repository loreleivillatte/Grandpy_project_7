import unittest
from unittest.mock import Mock, patch
import requests
from py_bot.views import app
from py_bot.utils import get_map, format_response, get_section


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status_code(self):
        response = self.app.get('/index')
        self.assertEqual(response.status_code, 200)


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.format = "4 Rue Baronie, 31000 Toulouse, France"
        self.formatted = " Rue Baronie"
        self.wiki = "La rue Baronie (en occitan : carrièra Veronica)" \
                    " est une rue du centre historique de Toulouse, en France."
        self.google = {'results': [{'formatted_address': self.format, 'geometry': {
            'location': {'lat': 43.601616, 'lng': 1.445087}}}]}

    def test_get_map(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.json.return_value = self.google
            lat, lng, address = get_map("test")
            self.assertEqual(lat, 43.601616)
            self.assertEqual(lng, 1.445087)
            self.assertEqual(address, self.format)

    def test_format_response(self):
        response = format_response(self.format)
        self.assertEqual(response, self.formatted)

    def test_get_section(self):
        response = get_section(self.formatted)
        self.assertEqual(response, "GrandPy Bot : " + self.wiki)


