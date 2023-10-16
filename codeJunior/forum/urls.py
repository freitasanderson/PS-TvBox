from django.urls import path
from forum.views import ForumIndexView

urlpatterns = [
    path('', ForumIndexView.as_view(), name="index-Forum"),
]
