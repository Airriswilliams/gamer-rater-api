from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from gamerraterapi.views import register_user, login_user
from rest_framework import routers
from gamerraterapi.views import GameView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView,'game')


urlpatterns = [
    # # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]