from rest_framework import routers
from rest_framework import urls
from django.urls import path, include
from registration.views import Registration, Login


router = routers.DefaultRouter()

urlpatterns = [
    path("registration", Registration.as_view()),
    path("login", Login.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path("", include(router.urls)),
]
