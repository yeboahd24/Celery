from django.conf.urls import url
from photos.views import PhotoView
from feedback.views import FeedbackView

urlpatterns = [
    url('', PhotoView.as_view(), name="home"),
    url('feedback/', FeedbackView.as_view(), name="feedback"),
]
