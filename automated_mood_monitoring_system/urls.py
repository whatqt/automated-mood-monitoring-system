from rest_framework import routers
from rest_framework import urls
from django.urls import path, include
from registration.views import Registration, Login
from data_acceptance.views import DataAcceptance
from data_processing.views import GetResponsesAi


router = routers.DefaultRouter()

urlpatterns = [
    path("api/v1/api/v1/registration", Registration.as_view()),
    path("api/v1/login", Login.as_view()),
    path("api/v1/data_acceptance", DataAcceptance.as_view()),
    path("api/v1/responses_ai", GetResponsesAi.as_view()),
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path("", include(router.urls)),
]
