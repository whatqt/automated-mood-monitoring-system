from rest_framework import routers
from rest_framework import urls
from django.urls import path, include
from registration.views import Registration, Login
from data_acceptance.views import DataAcceptance



router = routers.DefaultRouter()

urlpatterns = [
    path("registration", Registration.as_view()),
    path("login", Login.as_view()),
    path("data_acceptance", DataAcceptance.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path("", include(router.urls)),
]
