from rest_framework import serializers
from .models import Topic, Comment, Reply

class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = ['url', 'id', 'author', 'content', 'created_at', 'comment']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'author', 'content', 'created_at', 'topic', 'replies']

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['url', 'id', 'title', 'content', 'author', 'created_at', 'comments']
