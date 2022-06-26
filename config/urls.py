from django.contrib import admin
from django.urls import path, include
from todo_lacrei.views import TodoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
