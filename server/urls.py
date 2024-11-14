from django.urls import path
from . import views

urlpatterns = [
    path('sse-stream', views.streaming_sse_view, name='sse_stream'),
]
