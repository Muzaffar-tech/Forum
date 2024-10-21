from django.urls import path
from .views import TopicListCreateView, CommentCreateView, ReplyCreateView

urlpatterns = [
    path('topics/', TopicListCreateView.as_view(), name='topic-list'),
    path('topics/<int:topic_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:comment_id>/replies/', ReplyCreateView.as_view(), name='reply-create'),
]
