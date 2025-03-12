from rest_framework import routers
from django.urls import path, include
from .views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

app_name='books'

urlpatterns = [
    path('', include(router.urls))
]
