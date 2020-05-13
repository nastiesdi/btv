from django.urls import path
from .views import post, FeedBackView

urlpatterns = [

    path('', post, name='new_feedback'),
    path(r'catalog/<str:product>/feedback/', FeedBackView.as_view(), name='feedback'),
    path('', post, name='new_feedback'),
]