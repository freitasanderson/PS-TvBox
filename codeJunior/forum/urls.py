from django.urls import path
from forum.views import ForumIndexView, SecaoView

app_name= 'forum'

urlpatterns = [
    path('', ForumIndexView.as_view(), name="index-Forum"),
    path('secao/<int:pk>/', SecaoView.as_view(), name="secaoView"),

]
