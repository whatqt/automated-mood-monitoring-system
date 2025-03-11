from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from json import dumps
from unittest.mock import patch, MagicMock
from django.db.models.query import QuerySet
from datetime import datetime
from .views import DataAcceptance



class TestDataAcceptance(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @patch("data_acceptance.views.SendData")
    def test_post(self, mock_send_data):
        data = {
            "thema": "test",
            "msg": "test"
        }
        send_data = MagicMock()
        mock_send_data.return_value = send_data
        mock_send_data.__getitem__.ruturn_value = send_data
        mock_send_data.send.return_value = None
        request = self.factory.post(
            "/data_acceptance",
            data
        )
        view = DataAcceptance.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 202)

