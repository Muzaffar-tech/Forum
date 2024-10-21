from rest_framework import serializers
from .models import Topic, Comment, Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'author', 'content', 'created_at', 'comment']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'topic', 'replies']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments']
