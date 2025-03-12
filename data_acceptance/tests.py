from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from json import dumps
from unittest.mock import patch, MagicMock
from .views import DataAcceptance
from django.contrib.auth.models import User
from json import dumps



class TestDataAcceptance(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="unit_test",
            password="unit_test",
        )


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
            dumps(data),
            content_type='application/json'
        )
        request.user = self.user
        view = DataAcceptance.as_view()
        response = view(request)
        response.render()
        print(response.content)
        self.assertEqual(response.status_code, 202)

    def test_get(self):
        request = self.factory.get(
            "/data_acceptance"
        )
        request.user = self.user
        view = DataAcceptance.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 302)