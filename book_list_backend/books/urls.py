from django.urls import path, include
from rest_framework import routers

from .views import BookListView

router = routers.DefaultRouter()
router.register(r'', BookListView, basename="books")

urlpatterns = [
    path('', include(router.urls)),
]
