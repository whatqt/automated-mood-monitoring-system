from django.test import TestCase
from unittest.mock import patch
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from .views import GetResponsesAi



class TestGetResponsesAi(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="unit_test",
            password="unit_test",
        )
        self.factory = APIRequestFactory()

    def test_get(self):
        request = self.factory.get(
            "/api/v1/responses_ai"
        )
        request.user = self.user
        view = GetResponsesAi().as_view()
        response = view(request)
        self.assertEqual(response.status_code, 302)

