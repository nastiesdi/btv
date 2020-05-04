from django.urls import path
from .views import post, FeedBackView

urlpatterns = [

    path('', FeedBackView.as_view(), name='feedback'),
    path('', post, name='new_feedback'),
]