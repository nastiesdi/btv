from django.urls import path
from .views import post, FeedBackView

urlpatterns = [
    path('', post, name='new_feedback'),
    path('', FeedBackView, name='feedback')
]